prompt = "\nWhat's one of your favorite foods?"
prompt += "\n(Enter quit when you're done listing foods.)\n"

active = True

while True:
    food = input(prompt)
    if food == 'quit':
        break
    else:
        print(f"\nMmmm, {food} sounds delicious.")
