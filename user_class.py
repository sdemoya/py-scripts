class User:
    """Models typical user information."""

    def __init__(self, username, first_name, last_name, email, age):
        """Initialize attributes to describe a user."""
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def greet_user(self):
        """Greet the user in the console."""
        return(f"\nHello, {self.username}!")

    def describe_user(self):
        """Summarize user information."""
        return(f"""
        Username: {self.username}
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Email: {self.email}
        Age: {self.age}
        """)

feona = User('feona1234567', 'Sam', 'Green', 'sammy@email.com', 35)

print(feona.greet_user())
print(feona.describe_user())

jim = User('prankster', 'Jim', 'Halpert', 'jim@theoffice', 30)

print(jim.greet_user())
print(jim.describe_user())

dwight = User('beets4eva', 'Dwight', 'Schrute', 'dwight@theoffice', 43)

print(dwight.greet_user())
print(dwight.describe_user())

stanley = User('leaveMeAlone', 'Stanley', 'Hudson', 'stanley@theoffice', 50)

print(stanley.greet_user())
print(stanley.describe_user())

pam = User('newYorkArtist', 'Pam', 'Beesly', 'pam@theoffice', 32)

print(pam.greet_user())
print(pam.describe_user())
