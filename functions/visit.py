prompt = "Where would you like to travel?"
prompt += "\n(Enter quit to exit the program.)\n"

active = True

#The below creates an infinate loop, press CTRL+C to exit.

#while active:
 #   destination = input(prompt)
  #  if destination == 'quit':
   #     continue
    #else:
     #   print(f"{destination.title()} sounds like a wonderful place to visit!")

# The below uses a continue statement to only print multiples of 3,
# by exiting the loop if that condition is not met.

current_number = 0
while current_number < 25:
    current_number += 1
    if current_number % 3 != 0:
        continue
    print(current_number)
