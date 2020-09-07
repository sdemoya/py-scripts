
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

la_vegan  = Restaurant('LA Vegan', 'Asian and American style')

la_vegan.describe_restaurant()

settabello = Restaurant('Settabello', 'Italian')

settabello.describe_restaurant()

sage = Restaurant('Sage', 'vegan brunch')

sage.describe_restaurant()

my_restaurant = Restaurant('Rosie Cakes', 'baked')

my_restaurant.number_served = 42

my_restaurant.describe_restaurant()

my_restaurant.served()

my_restaurant.number_served = 57

my_restaurant.served()

my_restaurant.increment_served(50)

my_restaurant.served()
