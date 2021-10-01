# Python Challenge Sudoku Solver - 9 by 9 Sudoku Solver
# Alden Dent
# 9/23/21

import numpy as np # Imports numpy library to use for handling arrays

board = np.zeros((9, 9), dtype = int) # Creates an empty array made up of 9 arrays of 9 integers
board[0] = [3, 0, 6, 5, 0, 8, 4, 0, 0] # Sets each array within the board array to the each row
board[1] = [5, 2, 0, 0, 0, 0, 0, 0, 0]
board[2] = [0, 8, 7, 0, 0, 0, 0, 3, 1]
board[3] = [0, 0, 3, 0, 1, 0, 0, 8, 0]
board[4] = [9, 0, 0, 8, 6, 3, 0, 0, 5]
board[5] = [0, 5, 0, 0, 9, 0, 6, 0, 0]
board[6] = [1, 3, 0, 0, 0, 0, 2, 5, 0]
board[7] = [0, 0, 0, 0, 0, 0, 0, 7, 4]
board[8] = [0, 0, 5, 2, 0, 6, 3, 0, 0]

def isSafe(row, column, num): # Checks if a certain number (num) can be put in a certain place (row, column) according to sudoku rules (number isn't already in row, column, or box already)
    for i in range(9):
        if num == board[row, i]: # Checks if the number already in the row
            return False

    for i in range(9): # Checks if the number is already in the box
        if num == board[i, column]:
            return False

    startRow = row - row % 3 # Finds the first row of the box that the number is in
    startColumn = column - column % 3 # Finds the first column of the box that the number is in
    for i in range(3):
        for j in range(3):
            if board[startRow + i, startColumn + j] == num: # Checks if the number is already in the box
                return False
    return True # Returns true if the number can be placed in that position

def solveBoard(row, column): # Function for solving the sudoku puzzle
    
    if row == 8 and column == 9: # Returns true if it has succesfully put a number in every place on the board
        return True

    if column == 9: # Moves on to the first column of the next row if it has reached the end of a row
        column = 0
        row = row + 1
    
    if board[row][column] > 0: # Only tries to solve for a place on the board if it doesn't already have a number in it (so it doesn't overwrite blank puzzle)
        return solveBoard(row, column + 1)
    
    for num in range(1, 10, 1):
        if isSafe(row, column, num): # Tests whether a number from 1 - 9 can be put in a certain place
            board[row, column] = num # If it can, it puts that number in that place
            
            if solveBoard(row, column + 1): # Tries solving the rest of the board
                return True
        board[row, column] = 0 # If it can't find a number 1-9 that will fit in that place, it
    
    return False               # returns false moving it back to the previous place

if (solveBoard(0, 0)):
    print(board) # Prints out the complete board if it can be solved
