# Datasets, Resources and Groups

Data is published in units called *datasets*. A dataset contains: information or [*metadata*](metadata.md) about the data; a number of *resources*, which hold the data itself. They are stored in an S3 bucket in Google Cloud Storage, or simply as a link, if the resource is elsewhere on the web.

## Exploring Datasets

By selecting `Datasets` you can see a list of all datasets on the platform. From the datasets page or an organization's page you can find a dataset you are interested in ([more details about searching datasets](metadata.md#find-data)). Selecting it will display the dataset page. At the top there are 3 tabs:
- `Dataset` - here you can see all the information about the dataset and a list of its resources, choosing a resource will take you to its page, where you can see details about it, manage and download it
- `Groups` - see any group the dataset is part of, or add it to new groups by selecting the group name and pressing `Add to group`
- `Activity Stream` - see the history of changes made to the dataset

## Creating a New Dataset

1. You can access the `Create Dataset` screen in two ways. Go to `Datasets` page, then select the `Add Dataset` button. Alternatively, go to `Organizations`, select the page for the organization that should own your new dataset. Provided that you are a member of this organization, you can now select the `Add Dataset` button.
2. Add [information](metadata.md#fields) about the data
3. Press `Next: Add Data`
4. This is where you will add one or more resources which contain the data for this dataset. Choose a file (`Upload` button, max file size = 1 GB) or link (`Link` button) for your data resource. Fill the other information on the page:
   - Name - a name for this resource, different resources in the dataset should have different names
   - Description - a description of the resource
   - Format - the file format of the resource
5. If you have more resources to add to the dataset, select `Save & add another`. When you have added all resources, press `Finish`.

## Managing Dataset

You can edit the dataset you have created, or any dataset owned by an organization that you are a member of, or any dataset, in which you have been listed as a collaborator with the Editor role or higher.

Go to the dataset’s page. Select `Manage`. Here you can:

### Edit Metadata or Delete Dataset

In the `Edit metadata` tab you can edit any of the fields. When you have finished, press the `Update Dataset` button to save your changes. Alernatively, you can delete the dataset by pressing `Delete`. The dataset is not completely deleted. It is hidden, so it does not show up in any searches. However, by visiting the URL for the dataset’s page, it can still be seen (by users with appropriate authorization), and *undeleted* if necessary. If it's important to completely delete the dataset - contact a sysadmin user.

### Manage a Dataset's Resources

In the `Resources` tab, you can add new resources to the dataset by pressing `Add new resource`, or, by selecting a resource, you can edit information about it. When you have finished editing, select the button marked `Update Resource` to save your changes. To delete the resource, press `Delete`.

### Dataset Collaborators

In the `Collaborators` tab, you'll see a list of all users that have been given special permissions to the dataset (**collaborators don't have to be members of the organization that owns the dataset**). From the list you can `Edit` (change their role) or `Delete` a collaborator. Add new collaborator by selecting `Add Collaborators` - choose their username, assign a role and press `Add Collaborator`.

**Collaborator Roles**:

- Member - can access the dataset if private, but not edit it
- Editor - can edit the dataset and its resources, as well as accessing the dataset if private
- Admin - in addition to managing the dataset, they can add and remove collaborators

## Groups

Groups are collections of datasets (**datasets in a group can be owned by different organizations**). They can also have members. By selecting `Groups` near the top of any page, you can find all the existing groups. Selecting a group will take you to its page where you'll find information about it and datasets that have been added to the group. Only sysadmin users can create groups, by going to the `Groups` page and pressing `Add Group`. Initially, the group has no datasets and only 1 member - the creator.

### Management

From the group's page, select `Manage`. On this page there are 2 tabs: `Edit` - where you can change information about the group or `Delete` it; and `Members` - you can see a list of all members, add or remove users from the group, or change their role.

**Group Roles**:

- Member - can add/remove datasets from the group
- Admin - do the same as a member + can edit group information, as well as manage the group's members
