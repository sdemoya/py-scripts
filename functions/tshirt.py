#This function accepts positional or keyword arguments.

def tshirt(text, size='medium'):
    """This function accepts size & text for a t-shirt."""
    print(f"You ordered a {size} t-shirt, that says:\n{text}")

#Let's test it with postional arguments.
tshirt('i <3 python', 'large')

#Let's call the function with keyword arguments in the wrong order.
tshirt(size='small', text='i <3 python')

#Now let's call it without changing the default value for size.
tshirt('python is more fun')

