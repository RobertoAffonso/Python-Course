decimals = range(0, 100)
my_range = decimals[3:40:3]
print(my_range == range(3, 40, 3))
print(range(0, 5, 2) == range(0, 6, 2))
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

r = range(0, 100)
print(r)

for i in r[::-2]:
    print(i)

print('=' * 50)

for i in range(99, 0, -2):
    print(i)

print('=' * 50)

print(range(100, 0, -2) == range(99,0)[::-2])

backString = "NATAS"
print(backString[::-1])

r = range(0, 10)
for i in r[::-2]:
    print(i)
