#Conditional Statements

foods = ['greens', 'rice', 'potatoes', 'carrots', 'peppers', 'seeds', 'grapes']

for food in foods:
    if food == 'greens':
        print("Eat your", food)
    else:
        print("Better skip the", food)

food = 'cake'

if food not in foods:
    print(f"{food.title()} is not on the list of approved foods.")
else:
    print("Yes, ",food, " is an approved food.")

food = 'peppers'

if food in foods:
    print(f"Go on, have some {food}.")
else:
    print(f"Only have a small portion of {food}.")

# print(f"This is a test to see how {food}.title() prints.") That will not title the food variable because it is outside of the curly braces.  Instead it prints peppers.title() as if it were plain text.

