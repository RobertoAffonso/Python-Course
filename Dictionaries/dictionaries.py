fruit = {"orange": "A sweet, orange, citrus fruit",
         "apple": "Good for making cider",
         "lemon": "A sour, yellow, citrus fruit",
         "grape": "A small, sweet fruit growing in bunches",
         "lime": "A sour, green, citrus fruit"}

print(fruit)
print(fruit["grape"])
# A dictionary is a list of items that don't repeat, instead of accessing a certain item using an index, you will
# use a key instead, which is defined by the string before the colon.

fruit["pear"] = "an odd shaped apple"  # Adding a new entry to the dictionary
print(fruit)
# Every key in a dictionary is unique, so if you assign a new value to the same key, it will overwrite the current value
# assigned to that key
#
# for example:
fruit["pear"] = "green, odd shaped, and tastes ok"
print(fruit["pear"])
#
# Deletes a certain entry inside the dictionary, in this case, we are deleting "lemon"
del fruit["lemon"]
# WARNING, if you type del 'name of the dictionary' without specifying a certain key, the del command will delete the
# entire dictionary
#
# The '.clear()' function removes all entries from a certain dictionary
fruit.clear()
print(fruit)

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == 'quit':
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)
