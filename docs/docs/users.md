# Users, Organizations and Authorization

There are 2 types of users: regular and sysadmin. An account is not required to search for and find data, unless the information is private, but it is needed for all publishing functions and personalization features. The platform uses Keycloak to manage user identity and access. You can find the `Log in` button from the top right corner of any page.

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

### News Feed

At the top of any page, select the dashboard symbol. This shows changes to datasets, organizations and groups that you follow. It is possible to follow individual users to be notified of changes that they make. To start/stop following something, go to its dedicated page and select `Follow`/`Unfollow`. You can also select the `Activity Stream` tab to see all activities related to the object. You can enable email notifications for updates to things you follow by enabling `Subscribe to notification emails` from your profile settings.

## Organizations

Organizations have members and own datasets. You need to be a member of an organization in order to create datasets. Each organization can have its own workflow and authorizations, allowing it to manage its own publishing process. It also has a homepage, where users can find some information about the organization and search within its datasets, this can be accessed by going to `Organizations` and selecting the specific organization you want to explore. Only sysadmin users can create organizations, by going to the `Organizations` page and pressing `Add Organization`. Initially, the organization has no datasets and only 1 member - the creator.

### Management

Users with the Admin role can edit an organization's information and change the access privileges to the organization for other users. You can do so by going to the organization’s page and selecting the `Manage` button. The `Edit` tab lets you change organization information or `Delete` it. From the `Members` tab you can see a list of all members, add or remove users from the organization, or change their role.

### User Roles

A user in an organization can create a dataset owned by that organization.

- Member - can see the organization’s private datasets
- Editor - anything a member can do + can edit and publish datasets
- Admin - anything an editor can do + can add, remove and change roles of organization members
