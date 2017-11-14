
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("{}".format(alphabet[1:5:2]))


small_decimals = range(0, 10)

my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))

o = range(0, 100, 4)
print(o)
p = o[::5] # If you set a new value in the 'step' value, it will multiply the previously set value by the new one,
           # So in this case it will be 20
print(p)

for i in p:
    print(i)

phrase = input("Please enter a phrase: ")
reversedPhrase = ""

for i in phrase[::-1]:
    reversedPhrase += i

print("The original phrase is:{}".format(phrase), end='\n')
print("This is the phrase after being reversed: {}".format(reversedPhrase))
