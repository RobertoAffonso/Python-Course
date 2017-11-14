# instruments = ["Guitar", "Bass Guitar", "Drums", "Keyboard", "Trumpet"]
#
# with open("instruments.txt", 'w') as instruments_txt:
#     for inst in instruments:
#         # In case the file does not exist, Python will create a new file, however if the file does exist, it will be
#         # overwritten
#         #
#         # After printing the item stored in 'inst', Python will write the current item to the 'instruments_txt' file,
#         # hence why it is being specified.
#         print(inst, file=instruments_txt)

# instruments = []
#
# with open("instruments.txt", 'r') as instruments_txt:
#     for inst in instruments_txt:
#         instruments.append(inst.strip('\n'))
#
# print(instruments)
# for inst in instruments:
#     print(inst)

# ghost = ("Meliora", "Ghost BC", "2015", (
#     (1, "Spirit"), (2, "From the Pinnacle to the Pit"), (3, "Meliora"), (4, "Spoksonat")
# ))
#
# with open("ghost.txt", "w") as ghost_txt:
#     print(ghost, file=ghost_txt)

with open("ghost.txt", "r") as ghost_txt:
    contents = ghost_txt.readline()

ghost = eval(contents)

print(ghost)
title, artist, year, tracks = ghost
print(title)
print(artist)
print(year)
print(tracks)
