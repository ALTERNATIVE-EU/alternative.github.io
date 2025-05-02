# Users, Organizations and Authorization

## Overview

The Alternative platform implements a comprehensive user management and authorization system. This system defines different user types, roles within organizations, and access controls for datasets and features. Understanding these concepts is crucial for effectively using and managing the platform, whether you're a regular user, an organization member, or an administrator.

There are 2 types of users: regular and administrator. An account is not required to search for and find data, unless the information is private, but it is needed for all publishing functions and personalization features. The platform uses Keycloak to manage user identity and access. You can find the `Log in` button from the top right corner of any page.

## Profile

You can see your profile by selecting the button containing your picture and name at the top of any page. You can change the information about you, including what other users see about you by editing your profile. To do this, select the gearwheel symbol at the top of any page or go to your profile page and select `Manage`. Make the changes you want and then press `Update Profile`.

### API Tokens

API tokens are used in API calls or with the python library to access private datasets, that your account has rights to.

To generate an API token:

1. Go to your profile page
2. Select the `API Tokens` tab
3. Set a name for your token and click `Create API Token`
4. A green box appears above, containing your API token, make sure to copy it - you won't be able to see it again

Underneath the creation form you can see all your tokens. From the list you can also `Revoke` a token, that you don't need anymore.

### AI/ML API Tokens

AI/ML API tokens are used to access the AI/ML API. To generate an AI/ML API token:

1. Go to your profile page
2. Select the `AI/ML API Tokens` tab
3. Set a name for your token and click `Create AI/ML API Token`
4. Set expiration date and roles for the token
5. Click `Create AI/ML API Token`
6. A green box appears above, containing your AI/ML API token, make sure to copy it - you won't be able to see it again

### News Feed

At the top of any page, select the dashboard symbol. This shows changes to datasets, organizations and groups that you follow. It is possible to follow individual users to be notified of changes that they make. To start/stop following a dataset, organization, group, or user, go to their dedicated page and select `Follow`/`Unfollow`. You can also select the `Activity Stream` tab to see all activities related to the item. You can enable email notifications for updates to items you follow by enabling `Subscribe to notification emails` from your profile settings.

### Organizations

Organizations have members and own datasets. You need to be a member of an organization in order to create datasets. Each organization can have its own workflow and authorizations, allowing it to manage its own publishing process. It also has a homepage, where users can find some information about the organization and search within its datasets, this can be accessed by going to `Organizations` and selecting the specific organization you want to explore. Only administrator users can create organizations, by going to the `Organizations` page and pressing `Add Organization`. Initially, the organization has no datasets and only 1 member - the creator.

### Management

Users with the Admin role can edit an organization's information and change the access privileges to the organization for other users. You can do so by going to the organization's page and selecting the `Manage` button. The `Edit` tab lets you change organization information or `Delete` it. From the `Members` tab you can see a list of all members, add or remove users from the organization, or change their role.

### User Roles

User roles within an organization define the level of access and permissions a user has for that organization's resources. There are three roles, each building upon the permissions of the previous:

1. Member:
      - Can view the organization's private datasets
      - Can access and download data from the organization's datasets
      - Cannot make changes to datasets or organization settings

2. Editor:
      - Has all the permissions of a Member
      - Can create new datasets owned by the organization
      - Can edit and update existing datasets
      - Can publish or unpublish datasets
      - Cannot modify organization settings or manage other users

3. Admin:
      - Has all the permissions of an Editor
      - Can add new members to the organization
      - Can remove members from the organization
      - Can change roles of organization members
      - Can modify organization settings and information
      - Has full control over all datasets owned by the organization

To change a user's role:
1. Go to the organization's page
2. Click on the `Manage` button
3. Select the `Members` tab
4. Find the user in the list
5. Use the dropdown menu next to their name to select the new role
6. Click `Update Member`

<!-- ### AI/ML API Roles

To have access to the AI/ML API models, a user needs to have the `ai-ml-api-{model}` roles. Each model has its own role, for example, to use the `clinicaldata` model, a user needs to have the `ai-ml-api-clinicaldata` role.

To edit AI/ML API roles:

1. Only platform administrators can edit these roles
2. Administrators can add or remove roles through the Keycloak administration interface
3. To add a role to a user:
   - Log in to the Keycloak admin console
   - Navigate to the Users section
   - Select the user
   - Go to the Role Mappings tab
   - Add the desired `ai-ml-api-{model}` role from the Available Roles list
4. To remove a role, reverse this process by selecting the role from the Assigned Roles list and removing it

If you need a role added or removed, please contact a platform administrator.
-->