# Platform Features

## Overview

The ALTERNATIVE platform offers a comprehensive set of features designed to support collaborative research, data management, and analysis in the field of environmental toxicology. These features are built upon a robust cloud infrastructure, leveraging technologies such as Kubernetes, CKAN, and JupyterHub to provide a scalable and user-friendly environment for scientists and researchers.

## Data Sharing

The platform's data sharing capabilities are primarily powered by CKAN (Comprehensive Knowledge Archive Network), a web-based catalog platform for managing large datasets collaboratively. Key features include:

- **Organization-based Access Control**: Each consortium partner is represented as an organization, with customizable workflows and authorization mechanisms.
- **Flexible User Roles**: Users can be assigned roles such as Member, Editor, or Admin, each with varying levels of access and control.
- **Rich Metadata Support**: Datasets include default metadata fields, custom fields, and specialized metadata for scientific experiments.
- **Resource Management**: Multiple resources can be associated with each dataset, supporting various file formats and external links.
- **Data Visibility Control**: Datasets can be set as public or private, allowing for both open data sharing and restricted access scenarios.
- **Dataset Collaboration**: Users can be added as collaborators on specific datasets, with granular permission settings.

## Development Environment

JupyterHub is integrated into the platform to provide a powerful development environment for researchers and data scientists. Features include:

- **On-demand JupyterLab Servers**: Users get personalized workspaces with a rich set of tools for data analysis and visualization.
- **Multiple Programming Environments**: Support for Python, R, and other languages, with pre-configured environments and libraries.
- **Integration with Platform Data**: Easy access to datasets stored in CKAN through custom Python libraries.
- **Resource Optimization**: Automatic shutdown of inactive servers to manage platform resources efficiently.
- **Customizable Workspace**: Users can configure their JupyterLab interface with various plugins and extensions.

## Multi-user and Collaboration

The platform is designed to facilitate collaboration among diverse teams of researchers, scientists, and regulators. Collaborative features include:

- **Shared Datasets**: Users can share datasets within organizations or with specific collaborators.
- **Collaborative Notebooks**: JupyterHub supports multi-user access to notebooks, enabling real-time collaboration.
- **Version Control Integration**: Built-in support for Git, allowing users to manage and share code effectively.
- **Customizable User Experiences**: CKAN extensions allow for tailored interfaces for different user groups.

## Single Sign-On

To provide a seamless user experience across different components of the platform, Single Sign-On (SSO) has been implemented:

- **Keycloak Integration**: Uses Keycloak for centralized identity and access management.
- **Unified Authentication**: Users can access both CKAN and JupyterHub with a single set of credentials.
- **Secure Access Control**: Supports fine-grained access control and advanced security features like Two-Factor Authentication (2FA).

## Elasticity

The platform leverages cloud infrastructure and Kubernetes to provide elastic scaling capabilities:

- **Dynamic Resource Allocation**: Kubernetes enables automatic scaling of resources based on demand.
- **Efficient Resource Utilization**: Services can scale up or down to optimize performance and cost.
- **Storage Flexibility**: Utilizes various storage solutions, including block storage and S3, to accommodate different data storage needs.
- **On-demand Compute**: JupyterHub spawns user environments on-demand, efficiently managing computational resources.

These features collectively create a powerful, flexible, and secure environment for collaborative research and data analysis in the ALTERNATIVE project, supporting the complex requirements of environmental toxicology studies.