def order_sandwich(*toppings):
    """Summarize what comes on a sandwich."""
    print(f"You ordered a sandwich, with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

order_sandwich('veggie burger', 'mayo', 'lettice', 'tomato')

order_sandwich('portabello', 'vegan_chipotle_jack')

order_sandwich('veggie patty', 'chipotle mayo', 'peppers', 'kale', 'pickles', 'tomato')
