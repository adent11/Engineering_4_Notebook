# Python Program 02 - Quadratic Solver
# Alden Dent
# 9/16/21

from math import sqrt # Imports the square root function

def findDiscriminant(a, b, c): # This function calculates and returns discriminant
    discriminant = b ** 2 -4*a*c
    return discriminant
    
def findRoots(a, b, c): # This function finds the roots and returns them in a list
    root1 = round((-1*b - sqrt(b**2 - 4*a*c)) / (2*a), 3) # Quadratic formula for first root
    root2 = round((-1*b + sqrt(b**2 - 4*a*c)) / (2*a), 3) # Quadratic formula for second root
    return [root1, root2]

userInput = "" # Sets the user input to blank so the while loop runs by itself the first time

print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + x = 0")

while userInput != "x":
    a = int(input("Enter coefficient a: ")) # Asks for each of the coefficient
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))
    if  findDiscriminant(a, b, c) < 0: # Prints message if roots are imaginary
        print("There are no real roots")
    else:
        print("Root #1: " + str(findRoots(a, b, c)[0])) # Prints the first root
        print("Root #2: " + str(findRoots(a, b, c)[1])) # Prints the second root
    userInput = input("Press Enter to run again, press x then Enter to exit: ") # Asks for input to run again or quit

print("Program exited") # Message printed after program is exited
