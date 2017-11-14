import shelve

with shelve.open("bike") as bike:
    bike["maker"] = "Yamaha"
    bike["model"] = "Ninja 500"
    bike["color"] = "Green"
    # bike["Engine_size"] = "500"

    # del bike["Engine_size"]
    for key in bike:
        print(key)

    print('=' * 40)
    print(bike["maker"])
    print(bike["model"])

