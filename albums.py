def albums(artist, title, songs=None):
    """Store information about albums in a dictionary."""
    if songs:
        album = {'Title': title, 'Artist': artist, 'Songs': songs,}
        return album
    else:
        album = {'Title': title, 'Artist': artist,}

OK_Computer = albums('Radiohead', 'OK Computer', 12)
print(OK_Computer)

print("\n")

Art_Angels = albums('Grimes', 'Art Angels')
print(Art_Angels)
