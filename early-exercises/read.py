from sys import argv

script, filename = argv

print(f"We're going to read {filename} now.")

target = open(filename)

contents = target.read()

print(contents)
