  # Author_ = Roberto
ip = input("Please enter an IP Address: ")
sectionLength = 0
numberSegments = 0

for i in range(0, len(ip)):
    if ip[i] != '.':
        sectionLength += 1

    else:
        print("Length: {0}".format(sectionLength))
        sectionLength = 0
        numberSegments += 1

if ip == '':
    print("Please Insert something")
    sectionLength = 0
else:
    numberSegments += 1
    print("Length: {0}".format(sectionLength))
    print("Your ip address is: {0}, it contains {1} segments".format(ip, numberSegments))
