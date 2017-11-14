# table = []
#
# for n in range(1, 13):
#     result = n * 2
#     table.append("{} times 2 is {} ".format(n, result))
#
# with open("sample.txt", 'r+') as sample_text:
#     lines = sample_text.readlines()
#     print(lines)
#
#     # for item in table:
#     #     print(item, file=sample_text)
#     for line in lines:
#         print(line, end='')
#
with open("sample.txt", "a") as sample_text:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=sample_text)
        print('-' * 30, file=sample_text)





