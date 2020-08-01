# This script is a way to practice and review what I've learned so far.
# It code I've written not an exercise or tutorial. :)

string = "I hope to see humans on Mars in my lifetime."

print(f"""This is our original string: {string}\n""")

print(f"""Now let's try the .title() method: {string.title()}
 Cool! Looks like the .title() method capitalizes the first letter of each word.\n""")

'''It's pretty neat how you can use the triple " or ' to print a block of text without having to use \\n
OR
to create enfacto multi-line comments.'''
# I think I prefer using an octothrope because it changes the text's color and makes my code easier to read.

print(f"""Because I didn't assign the new value of string.title() to a variable, the change doesn't affect the value of our original string.
Just look what happens when I print "string":
\t{string}\n""")

# Side note, by learning python using a virtual server and the command line, I get the added bonus of learning vim shortcuts and tricks as I go. Yae!


print("Great, got that working. \n Now let's trying reassigning string.title() to itself like this: \n\t'string = string.title()'\n")

string = string.title()

print(f"It worked! The new value of \"string\" is: {string}\n")

string = string.upper()

print(f"""Let's capitalize all the letters using the .upper() method:
        \t {string}\n""")

string = string.lower()

print(f"""On to the .lower() method, which changes all letters in a string to lowercase.
        \t {string}\n""")

# The f-strings I've been using were introduced in Python 3.6. Prior to 3.6 the .format() method was used.

first_name = "Rosie"
middle_name = "Peanut"
last_name = "Butter"

full_name = "{} {} {}".format(first_name, middle_name, last_name)

print(full_name.upper())

print(f"{full_name} is the best cat that ever lived.")


# Fun fact, I learned about a new type of error with this last one. Forget quotation marks on your string and it will come back as undefined since python doesn't recognize Rosie as a string without them.

# Now, let's look at some methods that will help us deal with whitespace.

# First, rstrip(), which removes any white space from the right end of a string (after the string)

test = " hello "

print(test)

print(test.rstrip())

# Hmmm, they both look the same when printed to the console. Let's try to make it more clear.

test = "     hello     "

print(f"{test} world")

print(f"{test.rstrip()} world")

# Now that's more like it! Now let's use the lstrip() method, which does the same as above but before the left side. That is, it removes whitespace from before a string.

print(f"Well {test} there.")
print(f"Well {test.lstrip()} there.")


# Wouldn't it be great if we could strip the whitespace from both sides of the string at once? Well that's exactly what the strip() method does.

print(f"Well {test.strip()} there.")
