# Overview

The ALTERNATIVE platform is designed to provide remote access to AI/ML models through a well-documented API and model runtime environment, enabling seamless interaction for end users. This approach allows researchers, regulators, and other stakeholders to execute predictive models, submit input data, and retrieve computational results programmatically without requiring local installations. The platform is optimized for scalability and security, ensuring efficient execution of different types of models such as physiologically based kinetic (PBK) models, toxicodynamic (TD) models, and QSAR-based AI models. However, the platform does not include UI-based client applications for visual analysis, as it prioritizes an API-driven workflow for integration with existing analytical pipelines and external applications. Users are encouraged to integrate API outputs with custom visualization tools, data processing environments, or third-party platforms suited to their specific needs.

**This section outlines the step-by-step procedure how to obtaining an authentication token, and interacting with the ALTERNATIVE platform’s AI/ML models via the API.**

## Usage procedure

### User provisioning

User accounts are provisioned by an administrator in Keycloak, where each user is assigned with email address, username, first and last name, and an initial password. Upon first login, users must verify their email address and are required to change their initial password to enhance security. The admin assigns specific roles based on the user type, such as access to AI/ML APIs or Jupyter Notebook environments. These roles define the level of access and permissions within the ALTERNATIVE platform.

### Login in web platform

Once provisioned, users can log in to the ALTERNATIVE web platform using their username and password. The authentication system ensures secure access, and users are redirected to their dashboard upon successful login. After their first login, users must complete email verification and password change before gaining full access to assigned services.

### Generate AI/ML Token

To interact with the ALTERNATIVE APIs, users need an API token for authentication. This token is generated through the platform’s user interface. Users must navigate to the token management section, where they can generate, renew, or revoke access tokens. The generated token is required to authenticate API requests securely. You can find instruction how to obtain AI/ML API Tokens [Here](../../maintainer-guide/system-services/ai-ml-api/api-usage/authentication/)

### Navigate to Swagger or use CURL

The ALTERNATIVE platform provides an API documentation interface (Swagger UI) where users can explore available endpoints, review input/output structures, and test requests interactively. Alternatively, users can execute API calls programmatically using CURL or other HTTP clients such as Postman. Swagger UI allows users to interact with the API through a graphical interface, while CURL provides a command-line-based approach. Access the interactive documentation [Here](https://ai-ml-api.platform.alternative-project.eu/swagger).

### Authenticate with the token in client

To access the API, users must include the generated authentication token in their requests. This is typically done by adding the token to the Authorization header in API requests. When using Swagger, users can enter the token in the provided authentication field. In CURL, the token is passed using the -H 'Authorization: Bearer <TOKEN>' header.

### Enter input parameters

Each AI/ML model within the ALTERNATIVE platform requires specific input parameters for execution. These parameters can include chemical structures (SMILES), molecular descriptors, physiological properties, or other relevant data. Users should refer to the API documentation (Swagger UI) to understand the required inputs for each endpoint.

### Execute request against the API

After entering the required input parameters, users can submit a request to the API. The API processes the request, executes the corresponding AI/ML model, and returns prediction results. The response includes toxicity classifications, probability scores, simulated concentration-time profiles, or other model outputs. Users can retrieve and analyze the results either via Swagger UI, CURL, or programmatically through an API client.

### Example Qurl requests

#### AOP AI_MitDys

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/AOP/AI_MitDys/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "smiles": "C2C(N=Cc1ccccc1)=C(N(N2c3ccccc3)C)C"
}'
```
#### AOP ML_KEsMIEs

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/AOP/ML_KEsMIEs/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "smiles": "C2C(N=Cc1ccccc1)=C(N(N2c3ccccc3)C)C"
}'
```
#### DICTrank ML_apical_cardiotox

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/DICTrank/ML_apical_cardiotox/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "smiles": "C2C(N=Cc1ccccc1)=C(N(N2c3ccccc3)C)C"
}'
```

#### hERG

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/hERG/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "smiles": "C2C(N=Cc1ccccc1)=C(N(N2c3ccccc3)C)C"
}'
```

#### Multitask

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/Multitask/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "smiles": "C2C(N=Cc1ccccc1)=C(N(N2c3ccccc3)C)C"
}'
```

#### AHR

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/AHR/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "smiles": "C2C(N=Cc1ccccc1)=C(N(N2c3ccccc3)C)C"
}'
```

#### PBPK Doxorubicin

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/pbpk/doxorubicin' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "dose_mg": 60,
  "age": 50,
  "weight": 70,
  "height": 190
}'
```

#### PBPK httk

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/pbpk/httk' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "chem_name": "Bisphenol A",
  "species": "human",
  "daily_dose": 1,
  "doses_per_day": 1,
  "days": 15
}'
```

#### TK 2D

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/TK/2D/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "compound": "DOX"
}'
```

#### TK 3D

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/TK/3D/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "compound": "DOX"
}'
```

#### TD Lipidomics

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/TD/lipidomics/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "compound": "DOX"
}'
```

#### TD Metabolomics

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/TD/metabolomics/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "compound": "DOX"
}'
```

#### TD Proteomics

```bash
curl -X 'POST' \
  'https://ai-ml-api.platform.alternative-project.eu/TD/proteomics/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "compound": "DOX",
  "protein": "P16403"
}'
```