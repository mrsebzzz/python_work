def make_album(artist, album, number_of_songs=None):
    album_artist = {'artist': artist, 'album': album, 'songs': number_of_songs}
    return album_artist

while True:
    print("\nPlease enter an artist and album: ")
    print("(Enter 'q' at any time to exit program.)")

    artist = input("Arist: ")
    if artist == 'q':
        break

    album = input("Album: ")
    if album == 'q':
        break

    songs = input("Number of songs:")
    if songs == 'q':
        break

    formatted_name = make_album(artist, album, number_of_songs=songs)
    print(f"{formatted_name}")