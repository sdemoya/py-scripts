class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"{self.name} serves {self.cuisine} cuisine.")

restaurant = Restaurant('LA Vegan', 'vegan')

restaurant.describe_restaurant()
