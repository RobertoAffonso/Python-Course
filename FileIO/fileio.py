# lyrics = open('C:\\Users\\Rober\\Documents\\sample.txt', 'r')
# # In case you don't specify a path, Python will understand that the specified file is located in the project folder
#
# for line in lyrics:
#     if 'square' in line.lower():
#         print(line, end='')  # The " end='' " attribute, tells python not to space out the lines in the output
#
# lyrics.close()
#
# with open('C:\\Users\\Rober\\Documents\\sample.txt', 'r') as lyrics:
#     for line in lyrics:
#         if 'DEVIL' in line.upper():
#             print(line, end='')
#
# with open('C:\\Users\\Rober\\Documents\\sample.txt') as lyrics:
#     line = lyrics.readline()
#     while line:
#         print(line, end='')
#         line = lyrics.readline()

with open('C:\\Users\\Rober\\Documents\\sample.txt') as lyrics:
    lines = lyrics.readlines()
print(lines)

for line in lines:
    print(line, end='')
