# import random
#
# highest = 10
# answer = random.randint(1, highest)
#
# print("Please guess a number between 1 and {}: ".format(highest))
# guess = int(input())
#
# if guess != answer:
#     if guess < answer:
#         print("Guess Higher")
#     elif guess > answer:
#         print("Guess lower")
#     print("Please guess again: ")
#     guess = int(input())
#     if guess == answer:
#         print("Well Done, you have guessed it")
#     else:
#         print("Sorry, you have not guessed it correctly")
# else:
#     print("You got it first time")

import random

highest = 10
answer = random.randint(1, highest)

print("Please enter a number between 1 and {}".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Guess Higher")
    elif guess > answer:
        print("Guess Lower")
    else:
        print("You got it!")