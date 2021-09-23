# Python Challenge Sudoku Solver - 4 by 4 Sudoku Solver
# Alden Dent
# 9/21/21

import numpy

blankR1 = input("Enter the first row: ")
blankR2 = input("Enter the second row: ")
blankR3 = input("Enter the third row: ")
blankR4 = input("Enter the fourth row: ")
allPossibleRows = numpy.empty(24, dtype = object)
possibleR1 = numpy.empty(0, dtype = object)
possibleR2 = numpy.empty(0, dtype = object)
possibleR3 = numpy.empty(0, dtype = object)
possibleR4 = numpy.empty(0, dtype = object)
possibleRowsColumns = numpy.empty((0, 4), dtype = object)

def uniqueCharacters(numberSet):
    for number in numberSet:
        if numberSet.count(number) != 1:
            return False
    return True

def uniqueColumns(row1, row2, row3, row4):
    for num in range(len(row1)):
        if not uniqueCharacters(row1[num] + row2[num] + row3[num] + row4[num]):
            return False
    return True

def matchesBlank(blankRow, filledRow):
    return blankRow[0] in ("0", filledRow[0]) and blankRow[1] in ("0", filledRow[1]) and blankRow[2] in ("0", filledRow[2]) and blankRow[3] in ("0", filledRow[3])

def drawBoard(row1, row2, row3, row4):
    print(row1)
    print(row2)
    print(row3)
    print(row4)

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            for l in range(1, 5):
                testRow = str(i) + str(j) + str(k) + str(l)
                if uniqueCharacters(testRow):
                    if matchesBlank(blankR1, testRow):
                        possibleR1 = numpy.append(possibleR1, testRow)
                    if matchesBlank(blankR2, testRow):
                        possibleR2 = numpy.append(possibleR2, testRow)
                    if matchesBlank(blankR3, testRow):
                        possibleR3 = numpy.append(possibleR3, testRow)
                    if matchesBlank(blankR4, testRow):
                        possibleR4 = numpy.append(possibleR4, testRow)

for row1 in possibleR1:
    for row2 in possibleR2:
        for row3 in possibleR3:
            for row4 in possibleR4:
                if uniqueColumns(row1, row2, row3, row4):
                    arrayToAppend = numpy.reshape(numpy.array([[row1], [row2], [row3], [row4]]), (1, 4))
                    possibleRowsColumns = numpy.append(possibleRowsColumns, arrayToAppend, axis = 0)

print("Empty board is:")
drawBoard(blankR1, blankR2, blankR3, blankR4)

for solution in possibleRowsColumns:
    print("")
    print("A solution is")
    drawBoard(solution[0], solution[1], solution[2], solution[3])
