import json

filename = 'name.json'

with open(filename) as f:
    name = json.load(f)
    print(f"Welcome back, {name}!")


