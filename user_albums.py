def albums(artist, title, songs=None):
   """Store information about albums in a dictionary."""
   if songs:
        album = {'Title': title, 'Artist': artist, 'Songs': songs,}
        return album
   else:
        album = {'Title': title, 'Artist': artist,}
        return album

while True:
    print("What's your favoirte album?")
    print("Enter q at anytime to quit.")

    title = input("My favorite album is called ")
    if title == 'q':
        break

    artist = input("Who is the album by? ")
    if artist == 'q':
        break

    result = {'Title': title, 'Artist': artist,}
    print(f"result = {result}")

