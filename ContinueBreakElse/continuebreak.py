# shopping_list = ["Milk", "Pasta", "Rice", "Spam", "Eggs", "Bread"]
#
# for item in shopping_list:
#     if item == 'Spam':
#         continue  # 'continue' skips the current value, and forces the loop to begin the next iteration
#     print("Buy " + item)
#
# print('')  # Empty space just to organize the code :)
# print('')  # Empty space just to organize the code :)
#
# for item in shopping_list:
#     if item == 'Spam' or item == 'spam':
#         break  # 'break' terminates the current loop
#     print("Buy " + item)

meal = ["eggs", "spam", "bread", "cheese"]
nastyFoodItem = ''

for item in meal:
    if item == "spam":
        nastyFoodItem = item
        break
else:  # This else only executes, if the for loop was completed without being broken out of
    print("I'll have a plate of that")

if nastyFoodItem == "spam":
    print("Can i have anything without spam in it?")
