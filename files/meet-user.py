import json

name = input("What's your name? ")

filename = 'name.json'
with open(filename, 'w') as f:
    json.dump(name, f)
    print(f"See you next time, {name}!")

