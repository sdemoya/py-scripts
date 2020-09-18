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


def remember_number():
    """Return the user's stored favorite number."""
    num = get_stored_number()
    if num:
        print(f"My favorite number is {num} too!")
    else:
        num = get_number()
        print(f"I'll remember your favorite number when you come back!")

remember_number()
