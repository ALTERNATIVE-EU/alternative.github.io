# Storage

![Figure 2](images/storage.png)
**Figure 2: ALTERNATIVE cloud storage architecture**

The storage architecture within the ALTERNATIVE platform is especially designed to provide robust, scalable, and persistent data storage solutions. This is achieved by leveraging Kubernetes' powerful storage abstractions, namely `StorageClass`, `Persistent Volume Claim (PVC)`, and `Volume`. These abstractions play a crucial role in decoupling the applications from the underlying storage infrastructure, thereby enhancing flexibility and scalability.

### Dynamic Allocation of Data Volumes
The platform utilizes the dynamic provisioning capabilities of Kubernetes to allocate data volumes as and when needed. This approach ensures that storage resources are efficiently utilized, with volumes being created on-the-fly to meet the demands of the applications. It eliminates the need for pre-provisioning storage, thereby optimizing resource allocation and reducing overhead.

### Persistence and Reattachment
A key feature of the platform's storage strategy is the persistence of data, which is crucial for maintaining data integrity and continuity. Data volumes are designed to be persistent, meaning that the data remains intact even if the associated application is terminated or fails. These volumes can be seamlessly reattached to other instances of the application at a later point, ensuring data continuity and minimizing downtime.

### Delegation of Scalability and Recovery
The platform delegates the responsibilities of scalability, recovery, and persistence to the cloud provider. By leveraging the cloud provider's robust infrastructure and services, the platform benefits from high scalability and efficient recovery mechanisms. This delegation allows the platform to focus on its core functionalities while relying on the cloud provider for maintaining the resilience and scalability of the storage infrastructure.

### Types of Storage Used
- **Block Storage:** The platform employs block storage as the primary file system for applications. This type of storage is ideal for scenarios where performance and low-latency are critical. Block storage provides the applications with high-speed access to their data, making it suitable for a wide range of workloads.
- **S3 Storage:** For the CKAN component of the platform, S3 storage is utilized. S3, known for its scalability and durability, is an object storage service that offers a simple and cost-effective solution for storing and retrieving large amounts of data. This choice of storage aligns well with CKAN's design goal of handling large datasets.

## S3 Storage

The ALTERNATIVE platform, particularly its CKAN component, has specific storage requirements due to the potentially large datasets containing omics data. To effectively manage these datasets, the platform employs S3 storage, a solution that is well-suited to handle large volumes of data.

### Scalability and Cost-Effectiveness of S3
S3 storage is chosen for its exceptional scalability and cost-effectiveness. It is adept at handling vast amounts of data, scaling seamlessly in response to the platform's storage needs. This scalability ensures that as the volume of omics data grows, the storage infrastructure can grow correspondingly without any significant challenges. Additionally, S3's pricing model, which typically involves paying only for the storage used, makes it a cost-effective solution for managing large datasets.

### Custom CKAN Integration with S3
The integration of CKAN with S3 storage has been achieved through a custom CKAN extension. This tailored extension enables CKAN to efficiently interface with the S3 storage, ensuring that the data storage and retrieval processes are optimized for performance and reliability.

### Direct Interface with S3
In the ALTERNATIVE platform, CKAN interfaces directly with the S3 storage, bypassing integration via the Kubernetes plane. This direct interaction streamlines the data flow between CKAN and S3, reducing complexity and potential bottlenecks that might arise from additional layers of integration.

### S3 Storage Service and Minio Library
The S3 storage service, provided by the cloud provider, utilizes the Minio library. Minio is an open-source object storage server that provides a high-performance, scalable solution and is fully compatible with Amazon S3 APIs. The use of Minio enhances the platform's ability to interact with S3 storage efficiently and securely.

### CKAN's API-based Data Exposure
It is important to note that CKAN does not directly expose the underlying S3 storage to end users. Instead, CKAN provides its own set of APIs for data access. This approach ensures that data access is controlled and secure, with CKAN serving as the intermediary layer managing user interactions with the stored data. This setup not only enhances security but also allows for the implementation of additional features and controls over how the data is accessed and used.

In summary, the use of S3 storage in the ALTERNATIVE platform, particularly for CKAN, is a strategic decision that addresses the specific needs of large-scale omics data management. The custom integration of CKAN with S3, the direct interface approach, and the utilization of the Minio library collectively ensure that the platform can handle large datasets efficiently while maintaining cost-effectiveness and security.

## Block Storage

In the ALTERNATIVE platform, block storage is the main type of data storage utilized by applications. This section delves into the specifics of how block storage is implemented and managed within the platform's architecture.

### Exposure as File System
Block storage is exposed to applications and services as a file system. This approach is familiar and intuitive for application developers, allowing them to interact with the storage using standard file operations. This method of exposure simplifies the process of reading from and writing to the storage medium, making it highly accessible for a variety of applications.

### Underlying Storage System
Block storage systems are most commonly disk-based, utilizing either Hard Disk Drives (HDD) or Solid State Drives (SSD). The choice between HDD and SSD is typically based on a trade-off between cost and performance. SSDs, with their faster data access speeds, are well-suited for high-performance requirements, whereas HDDs are often used for cost-effective storage solutions where speed is less critical.

### Consumption via Kubernetes APIs
Block storage within the platform is consumed through Kubernetes APIs, specifically through the use of volumes, Persistent Volume Claims (PVCs), and Storage Classes. This integration with Kubernetes APIs ensures a seamless and efficient management of storage resources within the platform's ecosystem. The platform offers the flexibility to define different storage classes, each tailored to meet varying performance requirements. This feature allows for the customization of storage resources based on specific needs of different applications or services. For instance, a storage class optimized for high I/O throughput can be used for data-intensive applications, while another class might be optimized for cost-effectiveness.

### Decoupling of Applications from Storage
A significant advantage of using block storage in this manner is the decoupling of applications from the physical storage. This abstraction is particularly beneficial in scenarios such as backup, disaster recovery, and migration. By abstracting the storage layer, applications can be easily moved, backed up, or restored without the need to manage the complexities of the underlying storage infrastructure. This decoupling not only enhances the flexibility of the storage system but also significantly improves the platform's resilience and agility in handling data.

## NFS

The platform deploys an NFS (Network File System) server additionally, to provide extra storage class for use by some applications. For instance, JupyterHub users require a shared data folder, which is used to collaborate on data available for multiple users at a time. This means that Jupyter user PODs need to attach to the same volume, which requires a storage class with mode `ReadWriteMany`. Since the cloud provider only offers block storage classes of type `ReadWriteOnce`, the NFS server is used to expose such volume.

## CKAN Storage

The CKAN application uses several types of storage:
- **Database:** Relational database is used to store the application state, including metadata, user data. Postgres is used in this case.
- **S3:** User defined data sets are mapped to S3 buckets.
- **Block storage:** For regular files like configuration needed by CKAN.

## JupyterHub Storage

![Figure 3](images/storage-jupyter.png)
**Figure 3: Diagram of Jupyter Storage**

JupyterHub has more complex storage requirements compared to the other ALTERNATIVE services.

### Multi-user capability
Each user is dynamically allocated a Kubernetes POD which contains the Jupyter kernel and runtime for this user. The POD is ephemeral, but its data associated with the user must be persisted to a user volume, which is 10 GB. Each user is allocated such volume the first time after login and when the POD disappears due to session timeout or logout of the user, the volume remains. When the POD is recreated it attaches to the same volume and replays the state from the last session.

### Shared folder
Additionally, users request the feature to be able to share data directly in Jupyter via a shared folder. This folder is mapped to a static volume with size 20 GB and mode `ReadWriteMany`, because multiple PODs must be able to attach and write to it simultaneously. The `ReadWriteMany` volume is provided by the NFS server.

### Accessing CKAN data from Jupyter
A custom python library was developed for ALTERNATIVE users called `alternative-lib`. It simplifies the access to CKAN/S3 data from Jupyter and is hosted on GitHub as an open-source project.

## Databases

Postgres database is deployed within the Kubernetes plane. It is used by CKAN and Keycloak services. The Postgres leverages block storage underneath.
