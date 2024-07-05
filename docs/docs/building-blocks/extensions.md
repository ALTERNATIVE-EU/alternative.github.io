# ALTERNATIVE platform extensions

The CKAN extension mechanism serves as a powerful framework for enhancing and customizing the functionality of the CKAN open-source data management system. CKAN's extensibility allows developers to augment the platform's core features, tailoring it to specific needs and requirements. Extensions can be created to introduce new functionalities, improve visualization capabilities, or customize branding elements. This extensibility is particularly valuable in the context of the ALTERNATIVE cloud data platform, where CKAN serves as the foundational technology.

The following extensions were developed and implemented as part of the Task 6.6 “Implementation of Cloud Data Platform”.

| name                    | description |
| ----------------------- | ----------- |
| ckanext-alternative_theme | extension that changes the default theme of the platform |
| ckanext-cloudstorage    | extension that implements support for S3 Cloud Storage. This is a modified version of the ckanext-cloudstorage extension, which uses libcloud |
| ckanext-keycloak_auth   | extension that enables Keycloak authentication and user management |
| ckanext-extrafields     | extension that adds additional fields to dataset metadata, such as size and experiment info |
| ckanext-keycloak_access_token | extension that enables management of AI/ML API tokens in Keycloak |