# List Comprehensions

print("""We can use a list comprehension to combine
        a for loop and the creation of new elements
        into one line, while automatically appending
        each new element. \n
        squares = [value**2 for value in range(1, 11)]
        """)
# The above was taken from Python Crash Course 2nd Edition by Eric Matthes.

squares = [value**2 for value in range(1, 11)]
print(squares)



