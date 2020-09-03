class User:
    """Store and print information about individual users."""

    def __init__(self, username, first_name, last_name, email, age):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.age = age

    def describe_user(self):
        """Print a summary of user information."""
        user_description = f"Here is a summary of {username}'s user info:"
        #\t\tFirst Name: {first_name}
        #\t\tLast Name: {last_name}
        #\t\tEmail: {email}
        #\t\tAge: {age}\n"""
        print(user_description)

    def greet_user(self):
        """Greet the user with a message printed to the console."""
        greeting = f"Hello, {user_name}!"
        print(greeting)

keawa = User('keawa', 'Kea', 'Wa', 'kw@email.com', '27')

print(keawa.describe_user())
keawa.greet_user()

