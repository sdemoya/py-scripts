import json

def get_stored_number():
    """Retrieve stored number."""
    filename = 'store_number.json'
    try:
        with open(filename) as f:
            num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return num

def get_number():
    """Prompt user for their favorite number and store it in a JSON file."""
    num = input("What's your favorite number? ")
    filename = 'store_number.json'
    with open(filename, 'w') as f:
        json.dump(num, f)
    return num

print(get_stored_number())
print(get_number())


