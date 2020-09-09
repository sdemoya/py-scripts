messages = ['hello',
  "can't talk right now",
  "i'll call you back"]

sent_messages = []

archived_messages = []

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

def archive_messages(message_list):
    while message_list:
        archive = message_list.pop()
        print(f"Archiving: {archive}...")
        archived_messages.append(archive)

#Use a copy or slice of the sent_messages list to archive messages without emptying sent_messages.

archive_messages(sent_messages[:])

print("\n\n")
print(f"messages = {messages}")
print(f"sent_messages = {sent_messages}")
print(f"archived_messages = {archived_messages}")
