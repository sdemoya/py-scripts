# Let's try this again. I started this script but didn't save it before walking away and got booted off my virtual server. Whoops!

# This is just another little script for me to practice what I've learned so far.

print("An integer is a whole number, and a float is a number with a decimal point.\n The number twenty is displayed as each respectively below.")
print(int(20))
print( float(20))

print("Python will default to a float with any operation involving a float, even if the result is a whole number.")

print(5 / 2.5)

print(2 ** 4)

print(8 / 3)

print(8 % 3)

print(8 % 2)

print((5 * 2) ** 2 / 2)

print("You can use underscores to separate numbers and make them more human friendly, without changing the value of the number. It also doesn't matter where you put the underscores.")

big_num = 20_000_000
big_num2 = 2_00000_00

print(f"{big_num} is the same as {big_num2}")

print("See? They print out as the same number with no underscores.")

print("You can also assign multiple variables with a single line of code, such as, x, y, z = 1, 2, 3.")

x, y, z = 1, 2, 3

print(f"This is x: {x}")
print(f"This is y: {y}")
print(f"This is z: {z}")

print(x + y)

