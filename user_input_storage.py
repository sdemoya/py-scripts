#First, we define an empty dictionary.
pets = {}

#Next we set a flag so the program knows when to quit.
poll_active = True

#Then we start a while loop to run as long as our flag is set to True.
while poll_active:
    #Ask the user for their name(which will be our key)
    name = input("\nWhat's your name?\n")
    #Ask the user for their pet's name(which will be our value)
    pet = input("\nWhat's your pet's name?\n")
    #Store the user's answers in the dictionary defined above(line 2)
    pets[name] = pet
    #Ask the user if anyone else wants to take the poll.
    repeat = input("\nWhould anyone else like to answer this Pet's Poll?\n")
    #If the user says no, set the flag to False, which will in turn end the while loop.
    if repeat == 'no':
        poll_active = False
    #Print out the information we've gathered/show the results.
    for name, pet in pets.items():
        print(f"{name} belongs to {pet}.")
