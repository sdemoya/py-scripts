file = 'pythonCan.txt'

#Reads and prints file three times.
with open(file) as file_object:
    contents = file_object.read()
print(contents*3)


