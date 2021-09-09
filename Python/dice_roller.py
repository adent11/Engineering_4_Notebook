# Automatic Dice Roller

# Written by [Alden Dent]

from random import randint

print ("Automatic Dice Roller")

numSides = input("How many sides do you want")

while True:
    inStr = input("Press enter to roll again, press x to exit: ")
    if inStr == 'x':
        break #stops loop, goes to statement after loop
    print (randint(1, numSides))
