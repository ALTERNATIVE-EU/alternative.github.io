# Datasets, Resources, and Groups in CKAN

## Overview

This document provides comprehensive information about Datasets, Resources, and Groups in the ALTERNATIVE platform, which is built on CKAN (Comprehensive Knowledge Archive Network). It covers the fundamental concepts, creation processes, management techniques, and best practices for working with datasets, resources, and groups. This guide is essential for users who need to understand how data is organized, shared, and accessed within the ALTERNATIVE platform.

## General Information

CKAN is a powerful open-source data management system that forms the backbone of the ALTERNATIVE platform's data sharing capabilities. It provides a web-based interface for cataloging, storing, and accessing data, making it easier for organizations to publish and share their data with internal teams or external audiences.

### Datasets

Datasets are the core units of data in CKAN. A dataset is a collection of data resources (such as files, databases, or APIs) along with descriptive metadata. Datasets in CKAN:

- Represent a logical collection of related data resources
- Contain metadata describing the data, its source, and usage
- Can be public or private, depending on sharing settings
- Are typically owned by an organization or user
- Can be tagged, categorized, and grouped for easy discovery

### Resources

Resources are the actual data files or references that make up a dataset. In CKAN:

- A resource can be any type of file (CSV, Excel, PDF, etc.) or a link to an external data source
- Multiple resources can be added to a single dataset
- Each resource has its own metadata, separate from the dataset metadata
- Resources can be previewed, downloaded, or accessed via API depending on their type and configuration

### Groups

Groups in CKAN are collections of datasets that share a common theme. They provide an additional way to organize and categorize datasets beyond organizations. Key features of groups include:

- Datasets from different organizations can be part of the same group
- A dataset can belong to multiple groups
- Groups can have their own pages with description and branding
- They help in discovering related datasets across organizational boundaries
- Groups can have members with different levels of access

## Creating a New Dataset

To create a new dataset in the ALTERNATIVE platform:

1. From the 'Datasets' page, click the 'Add Dataset' button, or go to your organization's page and click 'Add Dataset'.
2. Fill in the required metadata fields:
   - Title (unique across the platform)
   - Description
   - Tags (for improved searchability)
   - License
   - Organization (dataset owner)
   - Visibility (public or private)
3. Click 'Next: Add Data'.
4. Add one or more resources to your dataset:
   - Upload a file or provide a link to the data
   - Give the resource a name
   - Provide a description of the resource
   - Specify the format of the resource
5. Click 'Finish' when you've added all resources.

## Managing Datasets and Resources

### Editing Datasets

To edit an existing dataset:

1. Navigate to the dataset's page.
2. Click 'Manage'.
3. In the 'Edit metadata' tab, you can modify any of the fields.
4. Click 'Update Dataset' to save your changes.

### Managing Resources

To manage resources within a dataset:

1. Go to the dataset's 'Manage' page.
2. Click on the 'Resources' tab.
3. Here you can:
   - Add new resources by clicking 'Add new resource'
   - Edit existing resources by selecting them and modifying the information
   - Delete resources if needed

### Dataset Collaborators

You can manage collaborators for a dataset:

1. In the dataset's 'Manage' page, go to the 'Collaborators' tab.
2. Add new collaborators or edit/delete existing ones.
3. Assign roles: Member (view only), Editor (can edit), or Admin (full control).

## Groups Management

### Creating a Group

Note: Only system administrators can create groups in the ALTERNATIVE platform.

To create a new group:

1. Go to the 'Groups' page and click 'Add Group'.
2. Fill in the required information:
   - Name (used in URLs, can only contain lowercase letters, numbers, and dashes)
   - Description
3. Optionally, add an image to represent the group.
4. Click 'Create Group'.

### Adding Datasets to a Group

To add a dataset to a group:

1. Go to the dataset's page.
2. Click on the 'Groups' tab.
3. Select the group you want to add the dataset to from the dropdown menu.
4. Click 'Add to group'.

### Managing Group Membership

Group administrators can manage group membership:

1. Go to the group's page and click 'Manage'.
2. In the 'Members' tab, you can:
   - Add new members by entering their username and selecting a role
   - Change roles of existing members
   - Remove members from the group

Group roles include:
- Member: Can see the group's private datasets
- Editor: Can add/remove datasets from the group
- Admin: Can manage group membership and edit group properties

## Metadata

Metadata is crucial for organizing and discovering datasets. The ALTERNATIVE platform uses three types of metadata:

1. Default Metadata: Includes fields like title, description, tags, license, etc.
2. Advanced Metadata for Experiments: Custom fields for scientific experiments (e.g., culture medium, number of replicates, toxin type).
3. Custom Metadata: Arbitrary key/value pairs for additional dataset information.

## Best Practices

- Use clear, descriptive titles for datasets and resources.
- Provide comprehensive descriptions to aid in discovery and understanding.
- Use relevant tags to improve searchability.
- Always include licensing information.
- Keep metadata up-to-date, especially for frequently updated datasets.
- Use appropriate file formats for resources to ensure accessibility.
- Use groups to create meaningful collections of datasets that span multiple organizations.
- Keep group descriptions up-to-date to help users understand the purpose and content of the group.
- Regularly review group memberships to ensure appropriate access levels.

By following these guidelines, you can effectively create, manage, and share datasets, resources, and groups in the ALTERNATIVE platform, facilitating collaboration and data accessibility across the project.