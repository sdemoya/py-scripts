# colors = ['blue', 'green', 'yellow', 'red', 'purple']

# print(f"Here's our new list: ", colors)

print("Let's start things off with the range() function.")

print("The range() function takes three arguments: (start, stop, step).")

counter = list(range(1, 30))

print("""Actually, it might be easier to start with a list of numbers.
        Luckily, we can easily create a  list using range() wrapped in the list constructor like so:
        counter = list(range(1, 30))
        counter = """, counter)

skip_counter = list(range(0, 30, 2))

print(f"""We can also add a step parameter like so:
        step_counter = list(range(0, 30, 2))
        step_counter = """, skip_counter)

print("""\nYou may have noticed that the list stops short of the stop parameter.
So if I wanted the number 30 included, I would pass 31 as the stop parameter.""")

print("Great, now let's do some simple maths.")

print("min(counter) = ", min(counter))

print("max(counter) = ", max(counter))

print("sum(counter) = ", sum(counter))


