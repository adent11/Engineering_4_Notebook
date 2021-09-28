# Python Challenge - MSP (Hangman)
# Alden Dent
# 9/21/21

head =    "   0" # Creates a string for each state of each part of the hangman's body
noArms =  "   |"
oneArm =  "  \|"
twoArms = "  \|/"
torso =   "   |"
oneLeg =  "  /"
twoLegs = "  / \ "

def drawHangman(lives): # Draws the hangman in the correct state given the amount of lives remaining
    print("---┐") # Draws the noose
    if lives == 7:
        print("") # No body parts
        print("")
        print("")
        print("")
    if lives == 6:
        print(head) # One body part, continues for the rest
        print("")
        print("")
        print("")
    if lives == 5:
        print(head)
        print(noArms)
        print("")
        print("")
    if lives == 4:
        print(head)
        print(oneArm)
        print("")
        print("")
    if lives == 3:
        print(head)
        print(twoArms)
        print("")
        print("")
    if lives == 2:
        print(head)
        print(twoArms)
        print(torso)
        print("")
    if lives == 1:
        print(head)
        print(twoArms)
        print(torso)
        print(oneLeg)
    if lives == 0:
        print(head)
        print(twoArms)
        print(torso)
        print(twoLegs)

word = input("Player 1, enter your word") # Gets the word from the first player
print("\n" * 50) # Prints a bunch of newline characters to clear the board
lives = 7 # Starts with 7 lives
guess = len(word)*"-" # Creates a new string made of a dash for each character in the word input that represents the guess
correctGuesses = 0 # Count of correct guesses
wrongGuesses = 0 # Count of wrong guesses
hintsUsed = 0 # Number of hints used
drawHangman(lives) # Draws the hangman
print(guess) # Print out the current guess
    
while lives > 0 and guess != word: # Only executes while the player still has lives and the word hasn't been guessed
    goodGuess = False # Boolean of whether the letter guessed is in the word
    guessedLetter = input("Guess a letter") # Gets letter guess from player 2
    for place in range(len(word)):
        if word[place] == guessedLetter: # Checks whether the guessed letter is the same as the letter in the original word
            guess = guess[:place] + guessedLetter + guess[place+1:] # Replaces the - with the correct letter in the guess
            goodGuess = True # Sets the goodGuess boolean to true
            correctGuesses = correctGuesses + 1 # Adds one to the counter of correct guesses
    if goodGuess == False:
        lives = lives - 1 # Subtracts one life
        wrongGuesses = wrongGuesses + 1 # Adds one to the counter of missed guesses
    drawHangman(lives) # Draws hangman and prints out missed letters and guess again
    print(guess)

if(lives == 0): # Says so if all lives have been used
    drawHangman(lives)
    print("You ran out of guesses! The word was " + word)
else: # Says so if the word has been correctly guessed
    print("You correctly guessed the word " + word)
