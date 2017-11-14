import shelve
########################################################################################################################
#
#
#
#
#
########################################################################################################################
#
# The 'with' block always closes the file once the block reaches its end
# with shelve.open("shelftest") as fruit:
#     fruit['orange'] = "a sweet, orange, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "sour, yellow, citrus fruit"
#     fruit['grape'] = "a small, sweet fruit, grow in bunches"
#     fruit['lime'] = "a sour, green, citrus fruit"
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
########################################################################################################################
#
#
# manually creating a shelf
#
########################################################################################################################
# Opens the 'shelftest' file
fruit = shelve.open("shelftest")

# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "sour, yellow, citrus fruit"
# fruit['grape'] = "a small, sweet fruit, grow in bunches"
# fruit['lime'] = "a sour, green, citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])

# while True:
#     dict_key = input("Please enter a fruit: ")
#
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# Also, a shelf key MUST BE A STRING, unlike a dictionary
ordered_keys = list(fruit.keys())
ordered_keys.sort()

for i in ordered_keys:
    print(i + " -- " + fruit[i])

# Closes the 'shelftest' file
fruit.close()

# print(fruit)





