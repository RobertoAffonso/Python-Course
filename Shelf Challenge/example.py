import shelve

books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "scrambled_eggs": ["eggs", "butter", "milk"],
                    "bean_on_toast": ["beans", "bread"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "tomato"]}

books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["wd40"]}

print(books["recipes"]["soup"])
print(books["maintenance"]["loose"])
books.close()
