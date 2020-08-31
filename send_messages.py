messages = ['hello',
  "can't talk right now",
  "i'll call you back"]

sent_messages = []

def show_messages(m):
    for message in messages:
        print(message)

show_messages(messages)

print("\n")

def send_messages(message_list):
    while messages:
        sending = messages.pop()
        print(sending)
        sent_messages.append(sending)

    print(f"""\nThe following messages have been sent:
    \t{sent_messages}
    \nThe following messages need to be sent:
    \t{messages}""")

send_messages(messages)


