
# Features

## Data sharing in CKAN

CKAN facilitates secure data sharing and exchange between permitted users and groups through its rich access control capabilities. All datasets and resources uploaded to CKAN can be assigned granular privileges dictating which users or organizations can view, access for analysis, edit metadata, or fully delete the assets.

Flexible organization hierarchies allow reflective sharing permissions, such as a folder visible to members of a specific department, or an analytics project workspace shared between different users collaborating tightly. Access requests can also be configured for privileged approvals before enabling wider dataset visibility.

Published open data is made publicly findable and accessible to all CKAN visitors. Private data restricted to members of the same group or organization can be easily shared for collaboration scenarios with audit logs tracking all access. Restricted datasets also benefit from CKAN features like ratings/comments, metadata enhancements, and discussions while remaining protected.

### CKAN Metadata

Metadata helps organize, find, and understand information better, acting as a helpful guide that tells you what you need to know about the stuff you're looking at or working with. CKAN provides a powerful metadata functionality, including default fields, custom fields and metadata extension for scientific experiments.

- **Default Metadata Fields:**

  | name           | description |
  | -------------- | ----------- |
  | name           | unique across the platform, should be brief but specific |
  | URL            | automatically filled based on title, but can be edited |
  | Description    | longer description of the dataset, including information such as what people need to know when using the data |
  | Tags           | tags that help people find the data linked with other related data |
  | License        | it is important to include a license, so that people know how they can use the data |
  | Organization   | organization, owner of the dataset |
  | Visibility     | public or private visibility of the dataset |
  | Source         | where the data is from |
  | Version        | version of the data |
  | Author         | name of the person or organization responsible for producing the data |
  | Author email   | an email address of the author, to which queries about the data should be sent |
  | Maintainer     | name of the person or organization responsible for maintaining the data |
  | Maintainer email | details for a second person responsible for the data |

- **Advanced Metadata for Experiments:** Because the project and datasets specifics related to experiment data, predefined metadata fields were implemented. When creating or editing a dataset a checkbox located above the custom metadata fields is available to show these extra fields.

  | name                  | description |
  | --------------------- | ----------- |
  | Culture medium        | select culture medium between 2 options (EBM2 or Maintenance) |
  | Number of replicates  | set number of replicates |
  | Number of cells/well  | set number of cells/well |
  | Ratio iPSC-CMs/HCAECs | set ratio iPSC-CMs/HCAECs |
  | Date of experiment    | the date of the experiment |
  | Toxin                 | select toxin between 4 options (Ami, Blank, Dox, TBBPA) |
  | Age type              | select age type between 2 options (Old or Young) |
  | Dimension             | select dimension between 2 options (2D or 3D) |
  | Category              | select category between 6 options (Chip sensors, In vitro assays, Metabolomics, Proteomics, Toxin targeted metabolomics, Transcriptomics) |
  | Content               | select content between 3 options (Cells, Culture media, Not applicable) |
  | Model                 | select model between 2 options (Dynamic or Static) |

- **Custom Metadata Fields:** Storing additional metadata for a dataset beyond the default metadata is a common use case. The ALTERNATIVE platform provides a simple way to do this by allowing you to store arbitrary key/value pairs against a dataset when creating or updating the dataset. These appear under the “Advanced metadata for experiments” section on the web interface and in the ‘extras’ field of the JSON when accessed via the API.

## Development environment based on JUPYTERHUB

JupyterHub is leveraged to provide a multi-user development environment for data scientists and engineers collaborating on analytical workloads. It provides on-demand access to ephemeral notebook servers and IDEs, configured dynamically with language kernels, libraries, attached storage volumes, and access privileges depending on the user and context.

Key advantages include scalability, as JupyterHub handles provisioning secure single-user workspaces on a Kubernetes cluster to serve users simultaneously. The workspace isolation also creates personalization allowing custom tool and dependency configuration per project needs. JupyterHub provides a rich interface over kernels like Python, R, and Scala for code, visualizations, documentation while integrating with version control and data platforms.

Overall JupyterHub enables self-service access data science workbenches with security, governance, and devops service delivery advantages through Kubernetes backend automation. Notebooks can be easily shared between users and published to broader teams as standardized workflows or ML models are created. The workspace environment keeps evolving via community-sourced JupyterHub extensions too.

## Multi-user & collaboration support

Supporting secure collaboration across diverse teams is a key requirement shaping the ALTERNATIVE platform software architecture and component integrations. The ability for project researchers, partner company scientists, and designated regulators to seamlessly access permitted datasets or analytical workflows facilitates improved transparency and oversight over model development stages.

Additional collaboration-enhancing platform capabilities span multi-tenant Jupyter notebooks with selective content visibility and CKAN extension points to customize experiences for different user groups.

### Dataset Collaborators:

In the Collaborators tab there is a list of all users that have been given special permission to the dataset (collaborators don't have to be members of the organization that owns the dataset). From the list the collaborators can be deleted or their role changed. Here are the collaborator’s roles and rights:

- **Member** - can access the dataset if private, but not edit it
- **Editor** - can edit the dataset and its resources, as well as accessing the dataset if private
- **Admin** - in addition to managing the dataset, they can add and remove collaborators

## Single sign on - SSO

A key integration between the CKAN-based ALTERNATIVE web application and the JupyterHub development environment is single sign-on (SSO) based on Keycloak. From the web UI, users can launch Jupyter workspaces without reauthentication, providing a seamless user experience.

