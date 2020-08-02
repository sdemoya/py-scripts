# And now for lists!

print("""Lists are ordered collections, defined using square brackets. []
        Within a list, elements are separated by commas.
        Elements may be accessed using their index (position), which begins at 0, not 1, as show below.
        list_name[index] i.e. planets[0]
        If you're not sure how many elements exist in a list you can use -1 to return the last item,
        -2 to return the second to last item, and so on.

        """)

local_solar_sys = ['mercuy', 'venus', 'earth', 'mars','jupiter', 'saturn', 'uranus', 'neptune']
inner_planets = ['Mercury', 'Venus', 'Earth', 'Mars']
gas_giants = ['Jupiter', 'Saturn']
ice_giants = ['Uranus', 'Neptune']
drawf_planets = ['Pluto']

print("Here's a list: ")
print(inner_planets)
print("This is index 0: ")
print(inner_planets[0])
print("This is index -1: ")
print(inner_planets[-1])

print("You can also modify elements in a list like so: list[index] = 'new_item'")

rosie_toys = ['string', 'turtle', 'fuzzy_ball']

print("\nHere's our list.")
print(rosie_toys)

rosie_toys[1] = 'crumpled_paper'

print("\nHere we've changed 'turtle' to 'crumpled_paper' at  index 1: ")
print(rosie_toys)

print("\nTurns out Rosie really like her turtle toy, so let's add it back in using the insert() method like so: \tlist.insert(index, 'element').")

rosie_toys.insert(2, 'turtle')

print(rosie_toys)

print("""\nWe can use also the append() method to add to the end of the list without affecting any other elements.
       \t list.append('new_element')""")

rosie_toys.append('feathers')

print("Here's our appended list: ", rosie_toys)
