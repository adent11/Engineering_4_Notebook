# Python Challenge Sudoku Solver - 9 by 9 Sudoku Solver with Pygame graphics window
# Alden Dent
# 9/30/21

import numpy as np # Imports numpy library to use for handling arrays
import os # Imports os, only used on the next line
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hides a message that prints by default when pygame is imported
import pygame # Imports pygame library which is used to make the graphics window

print("Python Sudoku Solver")
print("Press ESCAPE to exit window")
DELAY = int(input("Enter delay in milliseconds: ")) # Inputs the delay from the user

WIDTH, HEIGHT = 600, 600 # Width and height of the window
BOARD_OFFSET = 50 # Space between the edge of the window and the board
FRAME_WIDTH = 8 # Width of the lines of the board
BOX_WIDTH, BOX_HEIGHT = (WIDTH - 2*BOARD_OFFSET - 10*FRAME_WIDTH)/9, (HEIGHT - 2*BOARD_OFFSET - 10*FRAME_WIDTH)/9 # Sets the height and width of each box based on other constants

WHITE = (255, 255, 255) # RGB colors defined here for convenience
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (200, 200, 200)
FRAME_COLOR = BLACK

WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME) # Creates a window of size WIDTH, HEIGHT (600, 600), without a top bar for looks
clock = pygame.time.Clock() # Starts a clock
pygame.font.init() # Initializes pygame font module
MYFONT = pygame.font.SysFont('Microsoftsansserif', 40) # Creates font object

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

def exitCheck(): # Checks whether the program should be exited
    keys_pressed = pygame.key.get_pressed() # Gets the keys pressed
    if keys_pressed[pygame.K_ESCAPE]: # Quits if the escape key is pressed
        pygame.quit()
        exit()
    for event in pygame.event.get(): # Quits if window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def delay(t): # Function to delay while still checking exit conditions
    continueTime = pygame.time.get_ticks() + t # Sets the time at which the program should resume, current time + delay
    while pygame.time.get_ticks() < continueTime: # Waits until it has reached that time
        exitCheck() # Checks if user has tried to exit the window

def isSafe(row, column, num): # Checks if a certain number (num) can be put in a certain place (row, column)
    for i in range(9):        # according to sudoku rules (number isn't already in row, column, or box already)
        if num == board[row, i]:  # Checks if the number already in the row
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
    return True

def solveBoard(row, column):
    draw_window() # Draws what the board looks like every time it is changed by the solveBoard function
    exitCheck() # Checks if user has tried to exit the window
    delay(DELAY)

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

def draw_window(): # Function that handles drawing the window
    WIN.fill(BACKGROUND_COLOR) # Sets the background to the backround color
    pygame.draw.rect(WIN, FRAME_COLOR, pygame.Rect(BOARD_OFFSET, BOARD_OFFSET, WIDTH - 2*BOARD_OFFSET, HEIGHT - 2*BOARD_OFFSET)) # A black rectangle the size of the board
    for row in range(9):
        for column in range(9):
            pygame.draw.rect(WIN, BACKGROUND_COLOR, pygame.Rect(BOARD_OFFSET + FRAME_WIDTH*(row+1) + row*BOX_WIDTH, # Draws a box the same color as the background to make the 9x9 grid
                                                                BOARD_OFFSET + FRAME_WIDTH*(column+1) + column*BOX_HEIGHT, BOX_WIDTH,  BOX_HEIGHT))
    for row in range(9):
        for column in range(9):
            if board[row, column] > 0: # If the number isn't 0 (empty)
                numText = MYFONT.render(str(board[row, column]), 1, BLACK) # Renders then draws the number in the box, formatted to be centered
                WIN.blit(numText, (BOARD_OFFSET + FRAME_WIDTH*(column+1) + BOX_WIDTH*column + .5*(BOX_WIDTH-numText.get_width()), BOARD_OFFSET + FRAME_WIDTH*(row+1) + BOX_HEIGHT*row + .5*(BOX_HEIGHT-numText.get_height())))
    pygame.display.update() # Updates display, this is necessary to show any changes

draw_window() # Draws the window, then
delay(500)    # Pauses for half a second so the user isn't disorientated
solveBoard(0, 0) # Solves the board
while True: # Waits for user to exit the window
    exitCheck()
