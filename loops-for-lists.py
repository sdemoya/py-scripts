print("We can use for loops to complete an action on each item in a list.")

rosie_attributes = ['fluffy', 'smart', 'loyal', 'sweet', 'calm']

for attribute in rosie_attributes:
    print("Rosie is a", attribute, "kitty.")

for rose in rosie_attributes:
    print(f"{rose.title()} describes Rosie.")
