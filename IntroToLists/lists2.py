list_1 = []
list_2 = list()

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]  # This creates a list containing two other lists
print(numbers)  # This prints out the numbers variable which contains a list of the two lists `even` and `odd`

for number_set in numbers:
    print(number_set)
    for value in number_set:
        print(value)
