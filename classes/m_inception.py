from m_user import User
import m_admin

user447 = User('447', '447@fakemail.com')

print(user447.describe_user())

admin029 = m_admin.Admin('a029', 'a029@fakemail.com')

print(admin029.describe_user())

print(admin029.permissions.show_permissions())
