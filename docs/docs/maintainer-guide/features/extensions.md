# ALTERNATIVE Platform Extensions

## Overview

The CKAN extension mechanism is a powerful framework that enhances and customizes the functionality of the CKAN open-source data management system. This extensibility is crucial for the ALTERNATIVE cloud data platform, allowing us to tailor CKAN to our specific needs and requirements.

## Benefits of CKAN Extensions

- **Customization**: Adapt CKAN to specific project needs
- **Enhanced Functionality**: Add new features beyond CKAN's core capabilities
- **Improved User Experience**: Customize the interface and workflows
- **Integration**: Connect CKAN with other systems and services
- **Scalability**: Extend the platform's capabilities as project needs evolve

## ALTERNATIVE-Specific Extensions

The following extensions have been developed and implemented specifically for the ALTERNATIVE platform:

### 1. ckanext-alternative_theme

**Purpose**: Customizes the visual appearance of the platform

**Key Features**:

- Custom color scheme aligned with ALTERNATIVE branding
- Modified layout for improved user navigation
- Responsive design for various device types

### 2. ckanext-cloudstorage

**Purpose**: Implements support for S3 Cloud Storage

**Key Features**:

- Integration with S3-compatible storage services
- Efficient handling of large datasets
- Customized from the original ckanext-cloudstorage extension
- Uses libcloud for improved cloud storage interactions

### 3. ckanext-keycloak_auth

**Purpose**: Enables Keycloak authentication and user management

**Key Features**:

- Single Sign-On (SSO) capabilities
- Integration with Keycloak Identity and Access Management
- Enhanced security for user authentication
- Role-based access control

### 4. ckanext-extrafields

**Purpose**: Adds additional fields to dataset metadata

**Key Features**:

- Custom fields for experiment information
- Size metadata for improved dataset management
- Extensible structure for future metadata requirements

### 5. ckanext-keycloak_access_token

**Purpose**: Enables management of AI/ML API tokens in Keycloak

**Key Features**:

- Secure token generation and management
- Integration with AI/ML services
- User-specific API access control
- Token lifecycle management

## Implementing and Managing Extensions

1. **Installation**: Extensions are installed in the CKAN environment using pip or by cloning the extension's repository.
2. **Configuration**: Each extension is configured in the CKAN configuration file (`production.ini` or `development.ini`).
3. **Activation**: Extensions are activated by adding them to the `ckan.plugins` setting in the configuration file.
4. **Maintenance**: Regular updates and testing ensure compatibility with the core CKAN system and other extensions.


By leveraging these extensions, the ALTERNATIVE platform provides a tailored, robust, and feature-rich environment for managing and sharing scientific data and resources.