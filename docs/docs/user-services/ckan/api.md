# CKAN API

## Overview

The CKAN API is a powerful interface that allows programmatic access to CKAN's functionality. It enables developers and data scientists to interact with datasets, resources, and other CKAN features without using the web interface. The API is RESTful, using HTTP methods to perform operations and returning results in JSON format.

CKAN exposes most of its features through the API, making it the preferred method for working with datasets, especially for automation and integration purposes. 

## Key API Functionalities

CKAN's API offers a wide range of functionalities, including:

1. **Dataset Management**: Create, read, update, and delete datasets.
2. **Resource Management**: Add, modify, and remove resources within datasets.
3. **User and Organization Management**: Manage user accounts and organizations.
4. **Search and Discovery**: Search for datasets and resources using various parameters.
5. **Metadata Manipulation**: Update and retrieve metadata for datasets and resources.

## Common API Endpoints and Their Uses

Here are some of the most commonly used CKAN API endpoints and their functions:

### 1. Package (Dataset) API

- `package_list`: List all datasets in CKAN.
- `package_show`: Retrieve the metadata of a dataset.
- `package_create`: Create a new dataset.
- `package_update`: Update an existing dataset.
- `package_delete`: Delete a dataset.

### 2. Resource API

- `resource_show`: Get metadata about a resource.
- `resource_create`: Add a new resource to a dataset.
- `resource_update`: Update the metadata of a resource.
- `resource_delete`: Delete a resource from a dataset.

### 3. User API

- `user_list`: List users on the CKAN site.
- `user_show`: Return a user account.
- `user_create`: Create a new user.

### 4. Organization API

- `organization_list`: List or search organizations.
- `organization_show`: Return the details of an organization.
- `organization_create`: Create a new organization.

## API Usage Examples

### Python Examples

Here are some examples of how to use the CKAN API with Python:

- **Listing all datasets**:

    ```python
    import requests

    url = 'https://platform.alternative-project.eu/api/3/action/package_list'
    response = requests.get(url)
    datasets = response.json()['result']
    print(datasets)
    ```

- **Retrieving dataset metadata**:

    ```python
    import requests

    url = 'https://platform.alternative-project.eu/api/3/action/package_show'
    params = {'id': 'dataset-name-or-id'}
    response = requests.get(url, params=params)
    dataset_metadata = response.json()['result']
    print(dataset_metadata)
    ```

- **Creating a new dataset**:

    ```python
    import requests

    url = 'https://platform.alternative-project.eu/api/3/action/package_create'
    data = {
        'name': 'my-new-dataset',
        'title': 'My New Dataset',
        'owner_org': 'my-organization'
    }
    headers = {'Authorization': 'your-api-key'}
    response = requests.post(url, json=data, headers=headers)
    print(response.json())
    ```

### Curl Examples

Here are examples of how to use the CKAN API with curl:

- **Listing all datasets**:

    ```bash
    curl -X GET https://platform.alternative-project.eu/api/3/action/package_list
    ```

- **Retrieving dataset metadata**:

    ```bash
    curl -X GET https://platform.alternative-project.eu/api/3/action/package_show -d '{"id":"dataset-name-or-id"}'
    ```

- **Creating a new dataset**:

    ```bash
    curl -X POST https://platform.alternative-project.eu/api/3/action/package_create \
        -H "Authorization: your-api-key" \
        -H "Content-Type: application/json" \
        -d '{"name": "my-new-dataset", "title": "My New Dataset", "owner_org": "my-organization"}'
    ```

4. **Updating a dataset**:

    ```bash
    curl -X POST https://platform.alternative-project.eu/api/3/action/package_update \
        -H "Authorization: your-api-key" \
        -H "Content-Type: application/json" \
        -d '{"id": "existing-dataset-id", "title": "Updated Dataset Title"}'
    ```

5. **Deleting a dataset**:

    ```bash
    curl -X POST https://platform.alternative-project.eu/api/3/action/package_delete \
        -H "Authorization: your-api-key" \
        -H "Content-Type: application/json" \
        -d '{"id": "dataset-to-delete-id"}'
    ```

For more detailed information about the CKAN API, including all available endpoints and their parameters, please refer to the official [CKAN API documentation](https://docs.ckan.org/en/2.9/api/index.html).