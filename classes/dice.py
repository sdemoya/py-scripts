import random

class Dice:
    """Attempt to model rolling dice."""

    def __init__(self, sides):
        """Initialize attributes to describe a die."""
        self.sides = 6

    def roll_die(self):
        """Roll the die to generate a random number."""
        for i in range(self.sides):
            print('{:4.3f}'.format(random.uniform(1, self.sides)), end=' ')
        print()


six = Dice(6)

print(six.roll_die())

