# 1
# sum = 0
# for x in range (1, 51):
#     sum = sum + x
# print(sum, end=" ")

# 2

# sum = 0
# for


# 5 solution 1
# this code shows less efficent for a really, really, really beginer  because it has around call 300 times print function
# from random import randint

# for x in range(0, 15):
#     for y in range(0, randint(18, 20)):
#         print(" ", end="")
#     print(".oOo.")

from random import randint

# for line in range(0, 15):
#     lineString = ""
#     for spaceCounter in range(0, randint(18, 20)):
#         lineString = lineString + " "
#
#     lineString = lineString + ".oOo."
#     print(lineString)

for line in range(0, 15):
    lineString1 = ""
    for spaceCounter in range(0, randint(18, 20)):
        lineString1 = lineString1 + " "
    lineString1 = lineString1 + ".oOo."

    lineString2 = ""
    for spaceCounter in range(0, randint(25, 27)):
        lineString2 = lineString2 + " "
    lineString2 = lineString2 + ".oOo."

    print(lineString1, lineString2)
