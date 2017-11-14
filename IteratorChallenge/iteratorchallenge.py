item_list = ["knives", "body bags", "rope", "dagger", "chains", "laser beam", "rocks", "acid"]

new_iterator = iter(item_list)

number = len(item_list)

for item in range(number):
    print(next(new_iterator))

for i in item_list:
    print(i)
