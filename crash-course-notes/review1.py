# REVIEW

#LISTS
#   ordered, mutable collection defined by []
#   Access elements by index:
#                listname[index#]
#   Use string mehtods on elements within a list:
#                listname[index].method()


fruits = ['banana', 'orange', 'passonfruit', 'blueberries', 'apple']

print(f"fruits = {fruits}")

fruits.append('pear')

print(fruits)

fruits.insert(0, 'taco')

print(fruits)

del fruits[0]

print(fruits)

fav_fruit = fruits.pop(-1)

print(fav_fruit)

print(fruits)

fruits.insert(2, 'apples')

print(fruits)

fruits.remove('apples')

print(fruits)

fruits.sort()

print(fruits)

fruits.sort(reverse=True)

print(fruits)

fruits.reverse()

print(fruits)

print(len(fruits))

print("\n")

for fruit in fruits:
    print(f"I like to eat {fruit}!")

print("\n")

for number in range(1, 4):
    print(number)

count = list(range(1, 28))

print(count)

print("\n")

#List Comprehension
#   list_name = [expression for value in range(x,y)]

step_counter = [value**2 for value in range(2,17)]

print(step_counter)

odd_numbers = [pick for pick in range(1, 10, 2)]

print(odd_numbers)

even_numbers = [booger for booger in range(0, 11, 2)]

print(even_numbers)

print("\n")

print(fruits)

#Slicing a List
#   list_name[start#:end#+1]

print(fruits[2:4])

#   omit the first index and Python starts at 0

print(fruits[:5])

#   omit the last index and Python goes to the end

print(fruits[:])

#Copy a list with a slice.

new_fruits = fruits[:4]

print(new_fruits)

#TUPLES
#   immutable list
#   defined with or without parentheses
#   tuple_name = (value, value) or tuple_name = value, value

dimensions = (300, 150)

print(dimensions[0])
print(dimensions[-1])

#   even though a tuple is immutable, you can associate a new tuple with the
#   variable, effectively writing over it.

dimensions = 200, 300

print(dimensions)
