# Tuples are a set of ordered data, kinda like lists, except that they are immutable, so they can´t be changed

t = "a", "b", "c"  # This declares a tuple
print(t)  # This prints the tuple

print("a", "b", "c")  # Here we are printing a mere String

print(("a", "b", "c"))  # Here we are printing another tuple, notice that you have parentheses between the elements

meliora = "Meliora", "Ghost", 2015
reinkaos = "Reinkaos", "Dissection", 2006, (1, "Nexion 218"), (2, "Beyond the Horizon"), (3, "Starless Aeon")
majestic = "Ride Majestic", "Soilwork", 2015
carcass = "Surgical Steel", "Carcass", 2013
atoma = "Atoma", "Dark Tranquility", 2016
epitome = "Epitomen of Darkness", "Repugnant", "1998"

print(meliora)  # Prints out the 'Meliora' tuple
print(meliora[0])  # Prints out the item in position 0 in the meliora tuple
print(meliora[1])  # Prints out the item in position 1 in the meliora tuple
print(meliora[2])  # Prints out the item in position 2 in the meliora tuple

# Fun fact, the right hand side is always evaluated first, this is why line 23 works
epitome = "Epitome of Darkness", epitome[1], epitome[2]  # Here we are assigning a new variable containing the correct
# name for Repugnant's album
print(epitome)

# "Unpacking the tuple"
title, artist, year = atoma  # Here we are assigning multiple variables to certain items of the determined tuple
# title will be equal to reinkaos[0], artist = reinkaos[1], year = reinkaos[2]

print(title)  # Will print out the value of the 'title' variable
print(artist)  # Will print out the value of the 'Artist' variable
print(year)  # Will print out the value of the 'year' variable

# Tuples are generally used to store heterogeneous items
# You may use tuples when you store items that will not change, for example the title, genre, and release date for a
# computer game or a movie for example

print(reinkaos)

title, artist, year, track1, track2, track3 = reinkaos
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)


