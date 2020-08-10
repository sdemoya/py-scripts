#For Loops

print("We can use for loops to complete an action on each item in a list.")

rosie_attributes = ['fluffy', 'smart', 'loyal', 'sweet', 'calm']

for attribute in rosie_attributes:
    print("Rosie is a", attribute, "kitty.")

for rose in rosie_attributes:
    print(f"{rose.title()} describes Rosie.")

#Slicing

print("Slicing a list requires that you specify the index of the first and last elements you want to slice within square brackets. Similar to the range() function, Python will stop one item before the second index you specify. Let's use the list `rosie_attributes` to demonstrate.")

print("rosie_attributes = ", rosie_attributes)

print("rosie_attributes[1:4] = ", rosie_attributes[1:4])

print("If you leave off the starting index, Python will automatically begin at the first element, index 0.")

print("rosie_attributes[:3] = ", rosie_attributes[:3])

print("""The same is true of the ending index.
        rosie_attributes[0:] = """, rosie_attributes[0:])

print("""Let's see what happens when we don't speificy any index.
        rosie_attributes[:] = """, rosie_attributes[:])

print("Neat.\n")

print("""You can also use a negative index when specifying a slice.
        Remember how a negative index indicates distance fromt he end of a list?
        Check out the below examples.""")

print("rosie_attributes[-1:] = ", rosie_attributes[-1:])
