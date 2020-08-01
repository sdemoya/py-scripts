from sys import argv

script, username  = argv

prompt = '... '

print(f"Hi {username}. Let's talk about your cat.")
print("What is your cat's name?")
cat = input(prompt)

print("What is your cat's favorite toy?")
toy = input(prompt)

print("Is your cat actually a dog?")
dog = input('is or is not > ')
print(f"""
        So let me get this right...
        {cat} loves to play with {toy}!
        And {dog} a dog. Are you sure?
""")
answer = input(prompt)

print(f"OK, OK, {answer}! Got it.")
