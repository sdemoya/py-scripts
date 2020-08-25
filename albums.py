def albums(artist, title, songs=None):
    """Store information about albums in a dictionary."""
    album = {'Title': title, 'Artist': artist}
    return album

OK_Computer = albums('Radiohead', 'OK Computer', 12)
print(OK_Computer)


