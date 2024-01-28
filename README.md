 Peerxp Assessment

 
Given time 3days
done from 26/1/24 to 28/1/2024 

Note:some problems in front end,backend works fine can crud expenses


Introduction
Build a Personal Finance Management application that should allow users to record and track their expenses.

Assignment Details
Roles and Access Permissions
Users can have one of two roles: Admin or Member (Member is the default role).

Following are the access permissions for Admin and Member users.

Page or Feature
Admin access
Member access
Login page
Yes
Yes
Users
CRUD
No access
Create Expense
Yes (only their own data)
Yes (only their own data)
Update / Delete Expense
Yes (only their own data)
Yes (only their own data)
View Expenses
View (all members data)
View (only their own data)
⚠️
Users with an Admin role can just view other Members' expenses data. They cannot update or delete the data of other members.
List of Pages
Login page
The application should support basic email and password-based login. Users can sign in using their email address and password.
Registration and Forgot/Reset Password functionalities are not required.
Create Expense
Create Expense Form is a modal which will contain the following fields:
Fields
Description
Name
Name of the Expense Request (max length is limited to 140 characters only)
Date of Expense
Date Field 
Category
Dropdown with a set of predefined options such as {Health, Electronics, Travel, Education, Books and Others}.
Description
Text field
Amount
Integer field (restrict to Positive numbers only)
In addition to the aforementioned fields, the following fields will be automatically assigned when a POST request is made.
Fields
Description
Created by
Member ID who created the request.
Created at
DateTime when the Expense Request was created.
Updated at
DateTime when the Expense Request was updated.
Only if Expense is created successfully, show message “Expense created successfully!” otherwise, show “Expense create request failed.”
View Expenses
⚠️
Points to Note:
This page is accessible to both Members and Admins. Members can only access their own data, while Admins can access data for all users.
Both Admins and Members can only update or delete expenses that they have created. Even Admins cannot update or delete expenses created by other users.

The "View Expenses" page should contain a data table with the following columns:
Column Name
Remarks
Name
Category
Date of Expense
Amount
Updated at
Created by
Show “me” if Expense is created by the Logged-in user, otherwise show the User’s Email.
Action buttons
Edit and Delete buttons (use icons)
Each row in the data table represents an expense request.
If expenses were not created by the logged-in user (applies to admins), they will not see the Edit or Delete option.
The "Filter by Date" option, which includes a date picker, allows to filter the list of expenses based on the date of the expense request.
The "Search by Expense Name" function allows to search for expenses in the list by their name.
Editing Expenses
Editing an expense will use the same functionality as creating an expense form. The form will be displayed in a modal with existing data pre-filled, allowing users to make updates and save changes.
The "Created by" and "Created at" values will not update if an expense is edited.
Deleting Expenses
When deleting an expense, a confirmation prompt will be shown before the object is deleted from the database.
Users
⚠️
Points to Note:
UI Pages are not required for creating, updating, and deleting users. The default Django Admin page can be used instead.
To achieve the required login functionality, you can extend the default Django Users model if necessary.
Roles
The Admin Role can be implemented by setting the is_admin flag to True in the Users Model. 
However, you are free to choose the implementation design for Roles to meet the requirement stated in  section.

UI Design Reference
🖱️
To view the Design reference image in more detail, right-click on it and select "Open in new tab" and then maximize the image.
