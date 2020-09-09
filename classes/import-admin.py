from admins import User, Admin, Permissions

admin028 = Admin('admin028', 'a028@fakemail.com')

admin028.describe_user()

admin028.permissions.show_permissions()
