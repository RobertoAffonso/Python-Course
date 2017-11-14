
name = input("Please enter your name: ")

age = int(input("Now please enter your age: "))

if (age >= 18) and (age < 31):
    print("Welcome {0}! to the holiday!".format(name))
else:
    if(age < 19):
        print("Im sorry {0}, but you can't start your holiday, come back in {1} years".format(name, 19 - age))
    else:
        print("Im sorry {0}, but you are too old for the holiday".format(name))