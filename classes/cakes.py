#General Purpose Restaurant Class
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"{self.name} serves {self.cuisine} cuisine.")

    def served(self):
        """Prints a sentence about patrons served."""
        print(f"Rosie Cakes has served {self.number_served} patrons today.")

    def increment_served(self, patrons):
        self.number_served += patrons

#Let's bake some cakes!
class Bakery(Restaurant):
    """Specalized class to represent bakeries."""

    def __init__(self, name, cuisine):
        """Initialize attributes of parent class."""
        super().__init__(name, cuisine)

cakes = Bakery('Rosie Cakes', 'bakery')

print(cakes.describe_restaurant())
