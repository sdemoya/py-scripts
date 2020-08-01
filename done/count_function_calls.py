print("Welcome to my little script. I read that, theoretically, a function can be called in an infinite number of ways. Let's see how many ways I can come up with today.")

def nachoes(salsa):
    print(f"So you like your nachos with salsa {salsa}. Sounds delicious!")

print("Let's count how many ways I call this function:")

# update this later so you don't have to mannually print the count number
# count = 0

# def counter(count)
#    print(count + 1)

# counter(count)

print("1!")

salsa = "verde"

nachoes(salsa)

print("2!")

# Now you will need to include an argument when you run the script from the command line.

from sys import argv

script, salsa  = argv

nachoes(salsa)

print("3!")

print("What kind of salsa would you like? We have salsa verde, ranchera, roja, criolla, tauera and pico de gallo.")

salsa = input("> ")

nachoes(salsa)

