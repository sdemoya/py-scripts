class User:
    """Models typical user information."""

    def __init__(self, username, email):
        """Initialize attributes to describe a user."""
        self.username = username
        self.email = email
        self.login_attempts = 0

    def greet_user(self):
        """Greet the user in the console."""
        return f"\nHello, {self.username}!"

    def describe_user(self):
        """Summarize user information."""
        return(f"""
        Username: {self.username}
        Email: {self.email}
        Login Attempts: {self.login_attempts}
        """)

    def increment_logins(self):
        self.login_attempts += 1
        return f"{self.username} Attempted {self.login_attempts} Logins"

    def reset_logins(self):
        self.login_attempts = 0
        return self.login_attempts

