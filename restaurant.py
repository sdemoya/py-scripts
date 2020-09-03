class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"{self.name} serves {self.cuisine} cuisine.")

la_vegan  = Restaurant('LA Vegan', 'Asian and American style')

la_vegan.describe_restaurant()

settabello = Restaurant('Settabello', 'Italian')

settabello.describe_restaurant()

sage = Restaurant('Sage', 'vegan brunch')

sage.describe_restaurant()


