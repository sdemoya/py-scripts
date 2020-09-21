from name_fun import get_formatted_name

print("Enter 'q' at anytime to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")



print("""
    This exercise is from Python Crash Course by
    Eric Matthes and is intended for practice only.
    """)
