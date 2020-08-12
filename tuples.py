#Tuples

print("""A tuple is an immutable (un-changeable) list.
        They are defined by separating  each element by a comma,
        with option to enclose in parenthesis.
        For example if you want to define a tuple with only one element,
        it requires a trailing comma like so: my_tuple = (2,)
        (Note it doesn't generally make sense to create a tuple with only
        one element, but this can occur particullary when a tuple is
        generated automatically.
        They can be particularly useful for pairs of information, such as
        the dimensions of a shape or room.
        So what can we do with the imuutable data structures?
        To start with, we can loop over each element in a tuple.
        dimensions = (100, 50)

        for dimension in dimensions:
            print(dimension)

        And although we can't modify them, we can assign a new value to
        a variable which represents a tuple.

        dimesions = (70, 30)
        for dimension in dimensions:
            print(dimension)

        This second example above associates a new tuple with the variable 'dimensions'.""")

