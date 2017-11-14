# for i in range(10):
#     print("i is now: {}".format(i))
#
# i = 0
#
# while i < 10:
#     print("i is now: {}".format(i))
#     i += 1
#
# available_exits = ["east", "north east", "south"]
#
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#
#     if(chosen_exit == "quit"):
#         print("Game Over")
#         break
# else:
#     print("Aren't you glad that you got out of there?")
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Guess Higher")
    elif guess > answer:
        print("Guess lower")
    print("Please guess again: ")
    guess = int(input())
    if guess == answer:
        print("Well Done, you have guessed it")
    else:
        print("Sorry, you have not guessed it correctly")
else:
    print("You got it first time")