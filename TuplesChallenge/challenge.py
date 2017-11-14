
popestar = "Ghost", "Popestar", "2016", (
    (1, "Square Hammer"), (2, "Nocturnal Me"), (3, "I Believe"), (4, "Bible")
)

artist, title, year, tracks = popestar
print(artist)
print(title)
print(year)
# The for loop will loop through the tuple containing the tracks
# ergo, allowing us to separate each track with a tab break
for song in tracks:
    track, title = song
    print("Track Number: {}, Title: {}".format(track, title), '\t')


reinkaos = "Dissection", "Storm of the Light's Bane", 2002, (
    [(1, "At the fathomless depths"), (2, "Night's Blood"), (3, "Unhallowed")]
)

reinkaos[3].append((4, "Where dead angels lie"))

print(reinkaos)