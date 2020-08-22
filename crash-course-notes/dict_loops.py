#Looping Through a Dictionary

print("""We can loop thorugh all of a dictionary's key-value pairs,
        keys, or values.
        Looping Through All Key-Value Pairs:

                for key, value in dict.items():
                    do something


        Looping Through All Keys:

                for key in dict.keys():
                     print(key.title())

            Looping through keys is the default for looping through
            dictionaries, so you could also write:
                for key in dict:

            If we wanted to loop through the keys in a certain order,
            we could use the sorted() function like so:
                for name in sorted(favorites.keys()):
                    print(f"Hello, {name.title()}.")

        Looping Through Just Values:

                for val in dict.values():
                    do something
""")

rivers = {
        'nile': 'egypt',
        'colorado': 'united states',
        'amazon': 'peru',
        'chang jiang': 'china',
        'ob': 'russia',
        'zarie': 'congo',
        'mackenzie': 'canada',
        'sao francisco': 'brazil',
        }

print("\nOur dictionary includes the following rivers:")
for river in rivers:
    print(river.title())

print("\nThese rivers run through:")
for river in rivers.values():
    print(river.title())

print("\nNow let's list the rivers in alphabetical order:")
for river in sorted(rivers):
    print(river.title())

print("\nAnd now let's list it all together:")
for river, country in rivers.items():
    print(f"{river.title()}, {country.title()}")

print("\nAll together in alphabetical order:")
for river, country in sorted(rivers.items()):
    print(f"{river.title()}, {country.title()}")


