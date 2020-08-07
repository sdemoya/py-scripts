# colors = ['blue', 'green', 'yellow', 'red', 'purple']

# print(f"Here's our new list: ", colors)

print("Let's start things off with the range() function.")

print("The range() function takes three arguments: (start, stop, step).")

print("""Actually, it might be easier to start with a list of numbers.
        Luckily, we can use range() to quickly create it by using the list constructor like so:
        list(range(1,30))""")

counter = list(range(1, 30))

print(f"counter = ", counter)

skip_counter = list(range(0, 30, 2))

print(f"We can also add a step like so, list(range(0, 30, 2)), to get \n\t\t", skip_counter)

