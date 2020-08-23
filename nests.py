print("We can nest dictionaries and lists inside of one another.")

alien0 = {'color': 'blue', 'points': 5}
alien1 = {'color': 'yellow', 'points': 10}
alien3 = {'color': 'red', 'points': 15}

print("A List of Dictionaries")

aliens = [alien0, alien1, alien3]

for alien in aliens:
    print(alien)


print("A List Stored Inside of a Dictionary")

sandwich = {
        'bread': 'wheat',
        'veggies': ['lettice', 'tomato', 'avocado', 'onion'],
        'spread': 'garlic_aoli',
        'main': 'portobello',
        }

for ingredient in sandwich['veggies']:
    print(f"\n\t {ingredient}")

print("A Dictionary in a Dictionary")

solar_system = {
        'mercury': {
            'position': 'first',
            'moons': 0,
            },
        'venus': {
            'position': 'second',
            'moons': 0
            },
        'earth': {
            'position': 'third',
            'moons': 1,
            },
        'mars': {
            'position': 'forth',
            'moons': 2,
            },
        }

for planet, info in solar_system.items():
    position = f"{info['position']}"
    moons = f"{info['moons']}"
    print(f"{planet.title()} is {position} from the sun, and has {moons} moons.")
