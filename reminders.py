print("\n\t\t\tREMINDERS\t\t\t\n")

print("""
        Lists = ordered, mutable collection defined by []
            access elements by index:
                listname[index#]
            even use string mehtods on elements within a list:
                listname[index].method()
        """)


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
