import pickle

########################################################################################################################
#
#
# USING PICKLE TO STORE AND READ ITEMS FROM A BINARY FILE
#
#
########################################################################################################################

blaze = ("Silicon Messiah",
         "Blaze Bayley",
         '2000',
         ((1, "Stare at the sun"),
          (2, "Evolution"),
          (3, "Silicon Messiah"),
          (4, "Evolution")))

with open("blaze.pickle", "wb") as pickle_file:
    pickle.dump(blaze, pickle_file)

with open("blaze.pickle", "rb") as blaze_pickle:
    blaze2 = pickle.load(blaze_pickle)
print(blaze2)

album, artist, year, trackList = blaze2

print(album)
print(artist)
print(year)

for track in trackList:
    trackNumber, trackTitle = track
    print(trackNumber, trackTitle)


########################################################################################################################
#
#
# USING PICKLE TO STORE AND READ MULTIPLE ENTRIES
#
#
#
########################################################################################################################

blaze = ("Silicon Messiah",
         "Blaze Bayley",
         '2000',
         ((1, "Stare at the sun"),
          (2, "Evolution"),
          (3, "Silicon Messiah"),
          (4, "Evolution")))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("blaze.pickle", "wb") as pickle_file:
    pickle.dump(blaze, pickle_file, protocol=0)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=0)
    pickle.dump(25568, pickle_file, protocol=0)

with open("blaze.pickle", "rb") as blaze_pickle:
    blaze2 = pickle.load(blaze_pickle)
    even_list = pickle.load(blaze_pickle)
    odd_list = pickle.load(blaze_pickle)
    number = pickle.load(blaze_pickle)

    print(blaze2)

    album, artist, year, trackList = blaze2

    print(album)
    print(artist)
    print(year)

    for track in trackList:
        trackNumber, trackTitle = track
        print(trackNumber, trackTitle)

print('=' * 40)

for i in even_list:
    print(i)

print('=' * 40)

for i in odd_list:
    print(i)

print('=' * 40)

print(number)

print('=' * 40)
########################################################################################################################
#
#
############# WREAKING HAVOK #########################
#
#
########################################################################################################################

pickle.loads(b"cos\nsystem\n(S'del blaze.pickle'\ntR.")
