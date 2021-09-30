# Python Challenge Sudoku Solver - 4 by 4 Sudoku Solver
# Alden Dent
# 9/21/21

import numpy # Imports numpy library

blankR1 = input("Enter the first row: ") # Inputs each row as a string, with "0" for empty spaces
blankR2 = input("Enter the second row: ")
blankR3 = input("Enter the third row: ")
blankR4 = input("Enter the fourth row: ")
allPossibleRows = numpy.empty(24, dtype = object) # Creates an empty array with of 24 (4!) objects (which can be a string) to hold all valid rows (valid means all numbers in that set are unique)
possibleR1 = numpy.empty(0, dtype = object) # Creates an empty array for each row to hold all valid combinations for that row
possibleR2 = numpy.empty(0, dtype = object)
possibleR3 = numpy.empty(0, dtype = object)
possibleR4 = numpy.empty(0, dtype = object)
possibleRowsColumns = numpy.empty((0, 4), dtype = object) # Creates an empty two dimensional array to hold all valid row and column combinations

def uniqueCharacters(numberSet): # Function to determine if all characters in a string are unique
    for number in numberSet:
        if numberSet.count(number) != 1:
            return False
    return True

def uniqueColumns(row1, row2, row3, row4): # Function to determine if a combination of rows is valid
    for num in range(len(row1)):
        if not uniqueCharacters(row1[num] + row2[num] + row3[num] + row4[num]): # Checks if each column is valid
            return False
    return True

def matchesBlank(blankRow, filledRow): # Function to check if a row matches the filled in numbers in the empty board
    return blankRow[0] in ("0", filledRow[0]) and blankRow[1] in ("0", filledRow[1]) and blankRow[2] in ("0", filledRow[2]) and blankRow[3] in ("0", filledRow[3])

def drawBoard(row1, row2, row3, row4): # Function to print the board
    print(row1)
    print(row2)
    print(row3)
    print(row4)

for i in range(1, 5): # This massive (and disgusting) nest of for loops creates a list of all valid possibilities for each row
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

for row1 in possibleR1: # This other massive (and also disgusting) nest of for loops finds all possible solutions (valid combinations of rows)
    for row2 in possibleR2:
        for row3 in possibleR3:
            for row4 in possibleR4:
                if uniqueColumns(row1, row2, row3, row4):
                    arrayToAppend = numpy.reshape(numpy.array([[row1], [row2], [row3], [row4]]), (1, 4))
                    possibleRowsColumns = numpy.append(possibleRowsColumns, arrayToAppend, axis = 0)

print("Empty board is:")
drawBoard(blankR1, blankR2, blankR3, blankR4) # Prints the empty board

for solution in possibleRowsColumns: # Prints out all possible solutions
    print("")
    print("A solution is")
    drawBoard(solution[0], solution[1], solution[2], solution[3])
