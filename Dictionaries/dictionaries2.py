fruit = {"orange": "A sweet, orange, citrus fruit",
         "apple": "Good for making cider",
         "lemon": "A sour, yellow, citrus fruit",
         "grape": "A small, sweet fruit growing in bunches",
         "lime": "A sour, green, citrus fruit"}

print(fruit)

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("-" * 50)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(fruit.keys())
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

fruit_keys = fruit.keys()
print(fruit_keys)

fruit["Guava"] = "Pretty good overall"
print(fruit_keys)
