# Using Lists with While Loops

# While a for loop is effective for looping through a list,
# it shouldn't be used to modify the list because Python
# will have difficulty keeping track of the items in the list.
# Instead, use a while loop to modify a list as you loop through it.
# Using a while loop will allow you to collect, store & organize lots
# of input.

# Moving Items from One List to Another

needs_shots = ['bear', 'fido', 'fluffy']
vaccinated = ['rosie', 'zena']

print(f"To Be Vaccinated: {needs_shots}")
print(f"{vaccinated}'s vaccinations are up to date.")
while needs_shots:
    get_shots = needs_shots.pop()

    print(f"{get_shots.title()} is being vaccinated.")
    vaccinated.append(get_shots)

print(f"To Be Vaccinated: {needs_shots}")
print(f"{vaccinated} have all their vaccines.")

