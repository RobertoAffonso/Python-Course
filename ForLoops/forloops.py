# The for loops works like this: for each value of i, it executes the code until the specified range
# for example, if i had a range of 2 until 5, it would execute three times, because it reads "i from
# 2, until the number before 5, so its 2 until 5 - 1.
for i in range(1,21):
    print("i is now {}".format(i))

print("")  # Empty space just to organize the code :)

number = "9.234.357.968"
for i in range(len(number)):  # len() function returns the length of the String variable
    # number[i] means, return the character located at the position specified by the value of 'i'
    print(number[i])

print("")  # Empty space just to organize the code :)

number = "9.234.357.968"

for i in range(len(number)):
    if number[i] in "0123456789":
        print(number[i], end='')  # The 'end' variable set to '' overrides the default value of end
        # which is '\n', meaning to skip to a new line, by overriding
        #  this value, the for loop value now is being printed in a single line

print('')  # Empty space just to organize the code :)
print('')  # Empty space just to organize the code :)

number2 = "12.999.666.000"
cleanedNumber = ''  # Creates an empty variable to store a "clean" number2 variable

for i in range(len(number)):
    if number[i] in "0123456789":
        cleanedNumber = cleanedNumber + number[i]  # for each 'i' value, it concatenates a new character
        # To the cleanedNumber variable

newNumber = int(cleanedNumber)  # Here, the variable newNumber receives a converted cleanedNumber variable
# to an Integer

print("The number is: {}".format(newNumber))  # Here it prints the newNumber variable

print('')  # Empty space just to organize the code :)
print('')  # Empty space just to organize the code :)

########################################################################################################################

number3 = "129.999.888.777.666.000"
cleanedNumber2 = ''

# Here we have a different way to write the same code, instead of using number3[i], we use char, in other words it reads
# like this: For each char encountered in variable 'number3' do something
for char in number3:
    if char in "0123456789":
        cleanedNumber2 = cleanedNumber2 + char

newNumber2 = int(cleanedNumber2)
print("The number is {}".format(cleanedNumber2))

print('')  # Empty space just to organize the code :)
print('')  # Empty space just to organize the code :)

for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
    # In this example, the for loop goes through a list
    # of Strings, 'state' returns each String inside the
    # list.
    print("This parrot is " + state)
    # Alternatively we could use
    # print("This parrot is {}".format(state)

print('')  # Empty space just to organize the code :)
print('')  # Empty space just to organize the code :)

for i in range(0, 100, 5):  # The third element in the 'Range()' function means 'steps', in other words, how many
    # numbers it will skip until the next value
    print("i equals the number {}".format(i))

print('')  # Empty space just to organize the code :)
print('')  # Empty space just to organize the code :)

# In this example, we have a nested for loop, in other words, we have a for loop inside another for loop
for i in range(1,13):
    # Once 'i' is set, the second loop begins
    # Also, 'i' is only incremented after the 'j' loop ends
    for j in range(1, 13):
        print('{0} times {1} = {2}'.format(i, j, i * j), end='\t')
        # After 'j' reaches the last number in its range, the 'i' variable is incremented, beginning a new loop
    # print('#################')
# Basically the order is: 'i' begins with its first value being 1, after that it begins the 'j' loop by setting its
# first value as 1, and then it runs through its range from 1 to 13 - 1. Once it reaches the end of the defined range
# the variable 'i' is incremented in steps of 1, beggining the loop once again, until 'i' reaches its limit.
    print('')