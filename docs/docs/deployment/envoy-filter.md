# Alternative Envoy Filter

## Overview

This document describes the implementation and usage of a alternative Envoy filter designed for use in an Istio service mesh. The filter, written in Go, validates JWT tokens by checking if the token's ID has been revoked, as recorded in a database, and by verifying the token's signature. This ensures that only valid and active tokens are allowed, enhancing the security within the service mesh.

## Prerequisites

- Kubernetes cluster
- Service with deployment which will be protected by the filter
- Istio installed on the cluster
- A JWT token issuer, such as [Keycloak](https://www.keycloak.org/), to generate JWT tokens
- Docker
- PostgreSQL database

## Architecture

The alternative Envoy filter is registered as an HTTP filter in the Envoy proxy. The filter is written in Go. The filter is deployed as a sidecar container in the same pod as the service, and it intercepts all incoming requests to the service. The filter validates the JWT token signature and checks if the token ID has been revoked. If the token is valid, the request is forwarded to the service. If the token is invalid, the request is rejected. The filter also caches the token's revocation status to reduce the number of database queries, and the also caches the public key used to verify the token's signature. 

### Envoy and Istio Integration

The alternative filter is integrated with Envoy and Istio as follows:

1. The alternative filter is built as a shared object file (.so) and is registered as an HTTP filter in the Envoy proxy. The filter is deployed as a sidecar container in the same pod as the service.

2. The filter intercepts all incoming requests to the service. The filter validates the JWT token signature and checks if the token ID has been revoked. If the token is valid, the request is forwarded to the service. If the token is invalid, the request is rejected.

3. The filter caches the token's revocation status to reduce the number of database queries, and also caches the public key used to verify the token's signature.

### Database Interaction

The filter interacts with a database to check if the token ID has been revoked. The filter uses a PostgreSQL database to store the token IDs that have been revoked. The filter queries the database to check if the token ID is present in the database, and if the token ID is present, the filter rejects the request. The filter caches the token's revocation status to reduce the number of database queries.

## Getting Started

### Installation

1. Clone the repository:

```bash
git clone git@github.com:ALTERNATIVE-EU/auth-envoy-filter.git
```
1. Navigate to the `envoy-filter` directory:

   ```bash
   cd envoy-filter
   ```

2. Use `envoy-fitlter/database/schema.sql` to create the database schema in your PostgreSQL database.

3. Compile the envoy filter:

   ```bash
   docker compose run --rm go_plugin_compile
    ```

4. Create a PVC which will store the compiled envoy filter:

   ```bash
   kubectl apply -f manifests/pvc.yaml
    ```

5. Add volume to the service's deployment:

   ```bash
   kubectl patch deployment <depoyment-name> -n <namespace --type=json -p='[{"op": "add", "path": "/spec/template/spec/volumes/-", "value": {"name": "jwt-revocation-validation", "persistentVolumeClaim": {"claimName": "jwt-revocation-validation"}}}]'
    ```

6. Add volumeMount to the sidecar container:

   ```bash
   kubectl patch deployment <depoyment-name> -n <namespace> --type=json -p='[{"op": "add", "path": "/spec/template/spec/containers/1/volumeMounts/-", "value": {"mountPath": "/etc/istio/jwt-revocation-validation", "name": "jwt-revocation-validation"}}]'
    ```

7. Copy the envoy filter to the `revocation_filter` directory:

   ```bash
    kubectl cp -n <namespace> revocation_filter/revocation_filter.so -c istio-proxy $(kubectl get pod -n <namespace> -l app=<app-name> -o custom-columns=NAME:.metadata.name --no-headers):/etc/istio/jwt-revocation-validation/revocation_filter.so
    ```

8. Update the configuration in the `envoy-filter/manifests/envoyfilter.yaml` file to match your environment. Make sure to update `jwks_url` and `data_source_name` fields.

9.  Apply the envoy filter manifest:
    ```bash
    kubectl apply -f manifests/envoyfilter.yaml
    ```

### Configuration

The alternative filter is configured using the `envoy-filter/manifests/envoyfilter.yaml` file. The configuration options are as follows:

- `jwks_url`: The URL of the JWKS endpoint that contains the public key used to verify the JWT token signature.
- `data_source_name`: The data source connection string for the PostgreSQL database.
- `public_key_cache_ttl`: The time-to-live (TTL) for the public key cache.
- `revocation_status_cache_ttl`: The time-to-live (TTL) for the revocation status cache.

### Usage

1. Generate a JWT token using a JWT token issuer, such as [Keycloak](https://www.keycloak.org/).

2. Send a request to the service with the JWT token in the `Authorization` header:

   ```bash
   curl -H "Authorization: Bearer <JWT token>" http://<service-url>
    ``` 

3. The filter will validate the JWT token and forward the request to the service if the token is valid. If the token is invalid, the filter will reject the request.

4. Add the token to the revocation list:

   ```bash
   psql -h <database-host> -U <database-username> -d <database-name> -c "INSERT INTO revoked_tokens (token_id) VALUES ('<token-id>');"
    ```

5. Send a request to the service with the JWT token in the `Authorization` header:

   ```bash
    curl -H "Authorization: Bearer <JWT token>" http://<service-url>
    ```

6. The filter will reject the request because the token has been revoked.

### Trigger refresh cache

Send a request with header "X-Refresh-Cache: true", the envoy filter will trigger a manual refresh of the revocation status caches.
