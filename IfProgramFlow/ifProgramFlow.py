#
# name = input("Please insert your name: ")
# age = int(input("What is your age, {0}?: ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to join the army")
#     print("Please put an X in the ballot box")
# else:
#     print("Please come back in {0} years, {1}".format(18 - age, name))

# print("Please guess a number between 1 and 10")
# number = int(input())
#
# if number != 5:
#     if number < 5:
#         print("Guess higher")
#     else:  # Number is higher than 5
#         print("Guess lower")
#
#     number = int(input())
#     if number == 5:
#         print("Well Done, you have guessed it")
#     else:
#         print("Sorry, you have not guessed the correct number")
# else:
#     print("You got it first time!")

#age = int(input("How old are you?: "))

#if (age >= 16) and (age <= 65):
#if 15 < age < 66:
#
# if (age < 16) or (age > 65):
#     print("Enjoy your free time!")
# else:
#     print("Have a good day at work!")

# Fun fact: Python does not have a boolean data type, instead it has a 0 or 1 result
# 0 = false, 1 = true
# A 0 corresponds to any value that is declared to be empty
#
#x = input("Type something: ")

# if x:
#     print("You just typed in: {0}".format(x))  # In this case, X = 1, in other words it equals true
# else:
#     print("You did not type anything")  # In this case, X = 0, in other words it equals false
#
# The "Not" clause reverses the true or false results
#
# print(not true) # Returns false, since the reverse value for true, is false
#
# print(not false) # Returns true, since the reverse value for false, is true
#
parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I dont need that letter")