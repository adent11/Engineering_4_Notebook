# Python Challenge - MSP (Hangman) Spicy Version
# Alden Dent
# 9/21/21

from random import randint # Imports random library

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


while True: # While loop to repeat if players want to play again
    word = input("Player 1, enter your word") # Gets the word from the first player
    print("\n" * 50) # Prints a bunch of newline characters to clear the board
    missedLetters = "" # Empty string of letters missed
    lives = 7 # Starts with 7 lives
    guess = len(word)*"-" # Creates a new string made of a dash for each character in the word input that represents the guess
    correctGuesses = 0 # Count of correct guesses
    wrongGuesses = 0 # Count of wrong guesses
    hintsUsed = 0 # Number of hints used

    drawHangman(lives) # Draws the hangman
    print("Missed Letters: " + missedLetters) # Prints out the letters missed
    print(guess) # Print out the current guess
    
    while lives > 0 and guess != word: # Only executes while the player still has lives and the word hasn't been guessed
        goodGuess = False # Boolean of whether the letter guessed is in the word
        guessedLetter = input("Guess a letter") # Gets letter guess from player 2
        if guessedLetter not in missedLetters and guessedLetter not in guess and len(guessedLetter) == 1 and guessedLetter.islower(): # Ensures that the letter hasn't been guessed already and is a lower case letter
            for place in range(len(word)):
                if word[place] == guessedLetter: # Checks whether the guessed letter is the same as the letter in the original word
                    guess = guess[:place] + guessedLetter + guess[place+1:] # Replaces the - with the correct letter in the guess
                    goodGuess = True # Sets the goodGuess boolean to true
                    correctGuesses = correctGuesses + 1 # Adds one to the counter of correct guesses
            if goodGuess == False:
                missedLetters = missedLetters + " " + guessedLetter # Adds the incorrect guess to the string of incorrect guesses
                lives = lives - 1 # Subtracts one life
                wrongGuesses = wrongGuesses + 1 # Adds one to the counter of missed guesses
            drawHangman(lives) # Draws hangman and prints out missed letters and guess again
            print("Missed Letters: " + missedLetters)
            print(guess)
        elif guessedLetter in missedLetters or guessedLetter in guess : # Exception for if the letter has already been guessed
            print("That letter has already been guessed. Try again.")
        elif guessedLetter == "hint": # Gives a one letter hint if 'hint' is entered as the guess
            place = randint(0, len(word)-1)
            guess = guess[:place] + word[place] + guess[place+1:]
            hintsUsed = hintsUsed + 1
            drawHangman(lives)
            print("Missed Letters: " + missedLetters)
            print(guess)
        elif len(guessedLetter) != 1: # Exception for if multiple letters were entered
            print("Do not enter multiple letters. Try again.")
        elif not guessedLetter.islower(): # Exception for if the guess is not a lower case number
            print("Input must be a letter. Try again.")

    if(lives == 0): # Says so if all lives have been used
        drawHangman(lives)
        print("You ran out of guesses!")
    else: # Says so if the word has been correctly guessed
        print("You correctly guessed the word " + word)
    print(f"After {wrongGuesses} missed guesses, {correctGuesses} correct guesses, and {hintsUsed} hints used, the word was \"{word}\" ") # Prints the amount of wrong guesses, correct guesses, and hints used and the word
    if input("Do you want to play again? (y/n) ") == "n": # Asks if you want to play again and breaks the while loop if not
        break
