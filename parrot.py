# Now let's create a little "parrot" program, that repeats user input  until the user decides to quit.

prompt = "Hi, I'm Polly the Parrot. I repeat whatever you tell me until you type 'quit'."
prompt += "\nEnter something here: "

message = ""

while message != 'quit':
    message = input(prompt)
    if message != quit:
        print(f"\nGAWK, {message}")
   #Need to figure out how to stop "Polly" from repeating 'quit' before exiting.'


