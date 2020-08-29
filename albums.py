#def albums(artist, title, songs=None):
#   """Store information about albums in a dictionary."""
#    if songs:
#        album = {'Title': title, 'Artist': artist, 'Songs': songs,}
#        return album
#    else:
#        album = {'Title': title, 'Artist': artist,}
#        return album

#OK_Computer = albums('Radiohead', 'OK Computer', 12)
#print(OK_Computer)

#print("\n")

#Art_Angels = albums('Grimes', 'Art Angels')
#print(Art_Angels)

active = True

def your_albums(artist, title, songs=None):
   """Store information about albums in a dictionary."""
    #if songs:
        #album = {'Title': title, 'Artist': artist, 'Songs': songs,}
        #return album
    #else:
      #  album = {'Title': title, 'Artist': artist,}
    #return album

    while active = True:
        print("Please answer the questions below.
        \n Enter Q anytime to quit.")
        title = input("What is your album called? ")
        if title == "Q":
            break
        artist = input("Which artist or group created your album? ")
        if artist == "Q":
            break
        album = your_albums(title, artist)
        print(f"So you playing {album}? Nice!")


"""
active = True

def user_album(title, artist):
"""    """Creates dictionary to descibe an album with user input."""
"""    print("Type q at anytime to quit.")
    title = input("What the name of your favorite album? > ")
    artist = input("Whose is that by? > ")
       #  songs = input("Do you know how many songs are on it? > ")

        if title == 'q':
            active = False
        else:
            fav_album = {'Title': title, 'Artist': artist,}
            print(f"\nHere's your dictionary, {fav_album}\n")
"""
