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

for pet in needs_shots:
    print(f"{pet.title()} is in the waiting room.")

for pet in vaccinated:
    print(f"{pet.title()}'s vaccinations are up to date.")

while needs_shots:
    get_shots = needs_shots.pop()

    print(f"{get_shots.title()} is being vaccinated.")
    vaccinated.append(get_shots)
#I want to format this but I'm not sure how to do it.
#if len(needs_shots) => 0
#    print("All pets have been vaccinated. The waiting room is empty."
#else:
#    print(f"To Be Vaccinated: {needs_shots}")

for pet in vaccinated:
    print(f"{pet.title()} is fully vaccinated. Come back next year!")

