# #1
#
# S = int(input())
# M = int(input())
# L = int(input())
#
# happiness = 1 * S + 2 * M + 3 * L
# if happiness >= 10:
#     print("happy")
# else:
#     print("sad")

# 2

# P = int(input())
# N = int(input())
# R = int(input())
# total = N
# dayValue = N
# day = 0
# while total <= P:
#     dayValue = dayValue * R
#     total = total +dayValue
#     day = day + 1
#     if total > P:
#         break
# print(day)

#3



# N = int(input())
# largeX = -1
# smallX = 10000000
# largeY = -1
# smallY = 100000
#
# for count in range(1, N + 1):
#     x, y = input().split(',')
#     x = int(x)
#     y = int(y)
#     largeX = max(largeX, x)
#     smallX = min(smallX, x)
#     largeY = max(largeY, y)
#     smallY = min(smallY, y)
#
# print(str(smallX-1)+","+str(smallY-1))
# print(str(largeX+1)+","+str(largeY+1))

# 4


# T = input()
# S = input()
# list = []
# len = len(S)
# shift = S
# for times in range(1, len+1):
#     shift = shift[1:len] + shift[0:1]
#     list.append(shift)
#
#
# for win in range(0,len):
#     x = list[win]
#     y = T.find(x)
#     if y >=0:
#         print("yes")
#         a=1
#         break
#     else:
#         a =0
#
# if a !=1:
#     print("no")
# print(list)


#5
# import math
# M = int(input())
# N = int(input())
# # a, b, c, d=  input().split(' ')
# list = []
# n = M * N
# factor = int(math.sqrt(n))
# for i in range(1, factor + 1):
#     if n % i == 0:
#         x = i
#         y = n/i
#         sum = x + y
#         list.append(sum)
# lens = len(list)
#
# checkList=[]
# for x in range( 1, N+1):
#     for y in range(1, M +1):
#         num = int(input())
#         checkList.append(num)
# checkLen = len(checkList)
# print(checkList)
# for h in range(checkLen):
#     compare = checkList[h]
#     for r in range (lens):
#         compare2 = list[r]
#         if compare == compare2:
#             print("yes")
#             break
#

class ConnectedCell:
    row = None
    column = None
    visited = False
    def add_cell(self, row, column):
            self.row = row
            self.column = column

class Cell:
    row = None
    column = None
    number = None
    connectedCells = []
    def create_connected_cells(self, numberOfRow, numberOfColumn):
        for leftFactor in range(1, self.number + 1):
            if (self.number % leftFactor == 0):
                rightFacotr = self.number / leftFactor
                if (leftFactor <= numberOfRow and rightFacotr <= numberOfColumn ):
                    if (leftFactor != self.row or rightFacotr != self.column):
                        cell = ConnectedCell()
                        cell.add_cell(leftFactor, rightFacotr)
                        self.connectedCells.append(cell)


numberOfRow = int(input())
numberOfColumn = int(input())
grid = []

grid2 = []
for row in range(1, numberOfRow + 1):
    rowInput = input().split(' ')
    rowCells = []

    for number in rowInput:
        grid2.append(int(number))

        for column in range(1, numberOfColumn + 1):
             cell = Cell()
             cell.row = row
             cell.column = column
             cell.number = int(rowInput[column-1])
             cell.create_connected_cells(numberOfRow, numberOfColumn)
             rowCells.append(cell)

        grid.append(rowCells)


currentTargetNumber = numberOfRow * numberOfColumn
grid2[-1] = -1

while True:
    foundTargetNumber = False
    for i in range(0, len(grid2)):
        if (grid2[i] == targetNumber):
            foundTargetNumber = True
            grid2[i] = -1
            if (i == 0):
                print("Found")
                exit()
            else:
                newTargetNumber = ((i + 1) // numberOfColumn) * (i % numberOfRow)
                break
    if foundTargetNumber == False:
        currentTargetNumber = numberOfRow * numberOfColumn
    else







