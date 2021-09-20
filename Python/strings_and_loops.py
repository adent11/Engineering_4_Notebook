# Python Program 03 - Strings and Loops
# Alden Dent
# 9/20/21

def splitCharacters(word): # Returns a list with each character from the word passed to it
    return list(word)

userInput = input("Type in your text, then press Enter:") # Asks for and records the sentence input by the user

for word in userInput.split(): # Iterates through each word in the sentence
    for character in splitCharacters(word): # Iterates through each character in the word
        print(character) # Prints that word
    print("-") # Adds a - after each word
