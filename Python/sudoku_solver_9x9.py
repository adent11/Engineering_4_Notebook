# Python Challenge Sudoku Solver - 9 by 9 Sudoku Solver
# Alden Dent
# 9/23/21

import numpy as np

board = np.zeros((9, 9), dtype = int)
board[0] = [3, 0, 6, 5, 0, 8, 4, 0, 0]
board[1] = [5, 2, 0, 0, 0, 0, 0, 0, 0]
board[2] = [0, 8, 7, 0, 0, 0, 0, 3, 1]
board[3] = [0, 0, 3, 0, 1, 0, 0, 8, 0]
board[4] = [9, 0, 0, 8, 6, 3, 0, 0, 5]
board[5] = [0, 5, 0, 0, 9, 0, 6, 0, 0]
board[6] = [1, 3, 0, 0, 0, 0, 2, 5, 0]
board[7] = [0, 0, 0, 0, 0, 0, 0, 7, 4]
board[8] = [0, 0, 5, 2, 0, 6, 3, 0, 0]

def isSafe(row, column, num):
    for i in range(9):
        if num == board[row, i]:
            return False

    for i in range(9):
        if num == board[i, column]:
            return False

    startRow = row - row % 3
    startColumn = column - column % 3
    for i in range(3):
        for j in range(3):
            if board[startRow + i, startColumn + j] == num:
                return False
    return True

def solveBoard(row, column):
    
    if row == 8 and column == 9:
        return True

    if column == 9:
        column = 0
        row = row + 1
    
    if board[row][column] > 0:
        return solveBoard(row, column + 1)
    
    for num in range(1, 10, 1):
        if isSafe(row, column, num):
            board[row, column] = num
            
            if solveBoard(row, column + 1):
                return True
        board[row, column] = 0
    
    return False

if (solveBoard(0, 0)):
    print(board)
