# Python has many data types
#
# one of them is called an Integer, or a whole number without points, or, a number without a fractional part
#
# Example:
a = 16
#
# A number with a fractional part is called a float
#
# Example:
b = 3.5
#
#
#
c = 8
#
#
#
# + = sum operator, in other words, it adds the two variables
print(a + c)
#
#
# - = subtract operator, in other words it subtracts the two operators
print(a - c)
#
#
# * = multiply operator, in other words it multiplies both operators
print(a * c)
#
#
# / = division operator, in other words it divides both operators, in python it returns the
# resulting number as a float
print(a / c)
#
#
# // = same as the divide operator, except that it returns the resulting number as an integer
# instead of a float
print(a // c)
#
#
# % = remainder operator, in other words it gathers the remainder after a division between
# the variables
print(a % c)
#
#
#
#
parrot = "Norwegian Blue"
print(parrot)
#
# You can also print parts of a String, called a "Substring"
# Example
print(parrot[3])
print(parrot[0:9])
#
#
# If you don't specify a number in either of the first or second positions in
# [0:0], Python will grab the first number and print until the end of the string
# Example
print(parrot[:3])  # Prints from the beginning of the String, until the end of the String
#
print(parrot[3:])  # Prints from position 3 of the String, until the end of the String
#
print(parrot[-4:-2])  # Prints from position -4 of the String, and then it prints the next two characters of the String
#
print(parrot[0:6:2])  # Prints from position 0, and then it skips the characters until position 6, and prints each
#                     #character every 2 steps
#
print("Hello " * 5)  # Prints "Hello" 5 times
#
#
print("Hello " + "Sir")  # Concatenates both strings, and then it prints the result
#
#
today = "Sunday"
print("day" in today)  # The 'in' operator checks if the String 'today' contains the substring 'day'
#
#
print("Sun" in today)
#
#
print("fri" in today)
#
#
print("thur" in today)
#
#
print("bird" in "sky")
