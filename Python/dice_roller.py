# Automatic Dice Roller

# Written by [Alden Dent]

from random import randint

print ("Automatic Dice Roller")
print ("")
print ("How many sides do you want?")
numSides = input("")
print ("")
print ("How many dice do you want to roll?")
numRolls = input("")

while True:
    print("")
    inStr = input("Press enter to roll again, press x to exit: ")
    if inStr == 'x':
        break #stops loop, goes to statement after loop
    for x in range(int(numRolls)):
        print ("The value is:   " + str(randint(1, int(numSides))))
