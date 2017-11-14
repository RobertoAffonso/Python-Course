# my_list = list(range(0, 11))
# print(my_list)
#
# odd = list(range(1, 10, 2))
# even = list(range(0, 10, 2))
# print(odd)
# print(even)
#######################################################################################################
# a[start:end] # items start through end-1
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through end-1
# a[:]         # a copy of the whole array
# There is also the step value, which can be used with any of the above:
#
# a[start:end:step] # start through not past end, by step
# The key point to remember is that the :end value represents the first value
#  that is not in the selected slice. So, the difference beween end and start
#  is the number of elements selected (if step is 1, the default).
#
# The other feature is that start or end may be a negative number, which means
#  it counts from the end of the array instead of the beginning. So:
#
# a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items
# Python is kind to the programmer if there are fewer items than you ask for.
# For example, if you ask for a[:-2] and a only contains one element, you get an
#  empty list instead of an error. Sometimes you would prefer the error, so you have
#  to be aware that this may happen.

my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))  # Prints out the number corresponding to the position of the determined character
print(my_string[4])          # Prints out the substring corresponding to the number

small_decimals = range(0, 10)

print(small_decimals)
print(small_decimals[3])

odd = range(1, 10000, 2)

print(odd[985])
print(odd[985])

sevens = range(7, 1000000, 7)
x = int(input("Please enter a number less than one million: "))

if x in sevens:
    print("{} is divisible by seven".format(x))

print(small_decimals)

my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))
