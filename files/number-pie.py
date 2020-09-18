import json

def get_number():
    """Prompt user for their favorite number and store it in a JSON file."""
    num = input("What's your favorite number? ")
    filename = 'number.json'
    with open(filename, 'w') as f:
        json.dump(num, f)
    return num

print(get_number())

