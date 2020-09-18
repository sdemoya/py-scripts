import json

filename = 'name.json'

try:
    with open(filename) as f:
        name = json.load(f)
except FileNotFoundError:
    name = input("What's your name? ")
    with open(filename, 'w') as f:
        json.dump(name, f)
        print(f"See you next time, {name}.")
else:
    print(f"Welcome back, {name}!")

