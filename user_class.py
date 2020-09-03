class User:
    """Models typical user information."""

    def __init__(self, username):
        """Initialize attributes to describe a user."""
        self.username = username

    def greet_user(self):
        """Greet the user in the console."""
        return(f"Hello, {self.username}!")

feona = User('feona1234567')

print(feona.greet_user())
