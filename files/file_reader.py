print("Read and print an entire file.\n")

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.strip())

print("\nUse a for loop to read line by line.\n")

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

