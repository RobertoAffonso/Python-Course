# ipAddress = input("Please enter an IP Address: ")
# print(ipAddress.count("."))

# A list basically is a collection of a certain number of objects
# It can be a list of ints, strings, objects and even lists

parrot_list = ["not pinin'", "a stiff", "bereft of life"]  # this is a list of strings

parrot_list.append("a Norwegian Blue")  # .append adds a new item to the list
for state in parrot_list:
    print("The parrot is " + state)

even = [2, 4, 6, 8]  # this is a list of ints
odd = [1, 3, 5, 7, 9]  # this is another list of ints

numbers = even + odd
numbers.sort()  # this function alters the variable `numbers` however it does not create a new object

print(sorted(numbers))  # Prints out a new `numbers` object, however sorted out in the ascending order

#  Alternatively you can do this
#  numbers_in_order = sorted(numbers)
#  print(numbers_in_order)
