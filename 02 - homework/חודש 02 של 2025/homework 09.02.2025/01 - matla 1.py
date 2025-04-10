songs = []
song1 = input("enter song number 1: ")
song2 = input("enter song number 2: ")
song3 = input("enter song number 3: ")
songs.append(song1)
songs.append(song2)
songs.append(song3)
print(songs)
if song2 in songs:
    songs.remove(song2)
print("after remove middle: ", songs)

song4 = input("enter song number 4: ")
song5 = input("enter song number 5: ")
songs.append(song4)
songs.append(song5)
print(songs)
print(songs[1:-1])
