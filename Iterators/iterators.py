
# An Iterator is an object that returns a stream of a data one element at a time
# any object that supports iteration is called `iterable`, Strings and Lists are
# two examples of iterable objects

string = "1234567890"

# for char in string:
#     print(char)
# Behind the scenes there is an iterator that the for loop is using in order to print out each part of the string
# after the iterator reaches its limit, it reports an error that the for loop handles it and ends the loop

my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

