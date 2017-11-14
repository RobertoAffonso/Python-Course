age = 21
print("My age is: " + str(age) + " Years")  # The "str()" Method, converts the value inside the brackets to a String
#
#
print("My age is: {0} years".format(age))  # The {0} is called a replacement field, where the object inside the field
#                                          # will be converted to a String
#
print("There are {0} days in a week, they are called: {1}, {2}, {3}, {4}, {5}, {6}, and {7}".format(7,
"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"))
#
#
print("""January: {2}
February: {0}
March: {1}
April: {2}
May: {2}
June: {2}
July: {1}
August: {2}
September: {1}
October: {0}
November: {1}
December: {2}""".format(28, 31, 25))
#
#
# this is a way to format a number
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))
#
#
# Ye olde way
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i**2, i**3))
#
#
print("Pi is approximately {0:12.50f}".format(22 / 7))
#
#
# Ye olde way
print("Pi is approximately %12.50f" % (22 / 7))
