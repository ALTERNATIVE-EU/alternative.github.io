# Networking

## Overview

The network architecture of the platform is designed to support robust and efficient operations. At its core, the network is provisioned by a cloud provider, encompassing a comprehensive suite of fundamental virtual network functions. This includes:

- **Virtual Data Center (VDC)**
- An array of **subnets**
- A combination of **public and private IPs**
- **Network gateways**
- **Load balancers**
- **Ingress controllers**

These components collectively form the backbone of the network infrastructure, ensuring high availability and scalability.

## Kubernetes Networking

A central aspect of the network architecture is Kubernetes networking, as all applications are deployed on Kubernetes. This reflects a commitment to leveraging advanced container orchestration technology. The seamless integration between Kubernetes and the cloud provider is primarily due to the use of managed Kubernetes as a service. This integration not only simplifies operations but also enhances the reliability and efficiency of deployments.

### Container Network Interface (CNI)

In the Kubernetes environment, **Calico** is selected as the Container Network Interface (CNI) plugin. Calico is known for its simplicity, scalability, and security features, making it an ideal choice for Kubernetes networking needs.

## Application Networking

Regarding the networking of applications, a strong emphasis is placed on the isolation of network segments. This is achieved through the use of Kubernetes PODs and namespaces, providing a high degree of control and security. Traffic ingress is efficiently managed by an **NGINX-based Ingress controller**, ensuring that incoming traffic is effectively routed to the appropriate services.

## Security

Security is a paramount concern in the network architecture, particularly regarding data transmission. **TLS encryption** is employed, with **cert-manager** playing a crucial role in certificate management. This setup ensures the security of data in transit, providing assurance to users and stakeholders.

## DNS Configuration

DNS configuration is another key aspect of the network setup, handled by the **external-dns plugin**. This plugin automates the management of DNS entries, significantly reducing manual efforts and minimizing potential errors. All applications within the environment create entries in this zone, ensuring a cohesive and well-organized DNS structure.

## Conclusion

In summary, the network architecture is designed to not only meet the current demands of the applications but also to be adaptable and scalable for future needs, reflecting a commitment to advanced technologies and best practices.