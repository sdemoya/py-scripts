from m_user import User

#Permissions
class Permissions:
    """Dynamically models permissions a user or admin."""
    def __init__(self, permissions=['access personal profile', 'post', 'read']):
        """Initialize permissions attribute."""
        self.permissions = permissions

    def show_permissions(self):
        print(self.permissions)

    def add_permissions(self, new_permissions):
        self.permissions.append(new_permissions)
        print(f"""
        New Permissions:
        \t{self.permissions}
        """)


# Admins
class Admin(User):
    def __init__(self, username, email):
        """Initialize attributes from User & Permissions Classes"""
        super().__init__(username, email)
        self.permissions = Permissions()


admin027 = Admin('admin027', 'admin027@gmail.com')

print(admin027.describe_user())

print(admin027.permissions.show_permissions())

print(admin027.permissions.add_permissions('can create user'))

