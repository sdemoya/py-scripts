print("""A dictionary is a collection of key-value pairs,
        wrapped in curly braces {}. Each pair is connected
        with a colon : and separated from other pairs with
        a comma.
        user0 = {'name': 'Ally', 'color': 'purple', 'music': 'blues'}
        You can access a value using its key like so:
            user0['color']
        """)

user0 = {'name': 'Ally', 'color': 'purple', 'music': 'blues',}

#It's good practice to end a dictionary with a trailing comma so you can easily add new information.

print(user0['color'])

print("""You can also use get() to access values.
        If you try to access a value for a key that
        does not exist using the bracket notation,
        you will get an error.
        The get() method accepts an optional second
        arguement of what to return if the key does
        not exist.
        user0.get('music', 'No music found.')
        """)

print(user0.get('music', 'No music found.'))

print("Now let's try for 'y_coordinate.'", user0.get('y_coordinate', 'No data found.'))

print("""Because dictionaries are dynamic structures,
        you can also add key-value pairs to them using
        square brackets around the new key name like so:
            user0['x_coordinate'] = 0""")

print(f"user0 = {user0}")

user0['x_coordinate'] = 0

print(f"now user0 = {user0}")

print("You can also define an empty dictionary. user1 = {}")

print("As of Python 3.7 dictionaires retain the order in which they were defined.")

print("You can modify values in a dictionary the same way you add key-value pairs. user0['color'] = 'orange'")

user0['color'] = 'orange'

print(f"user0 = {user0}")

print("""To remove a key-value pair, use the del statement and
        square bracket notation like so:
                del user0['color']
    """)

del user0['color']

print(f"user0 = {user0}")


