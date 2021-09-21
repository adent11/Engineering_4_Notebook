# Python Challenge - MSP (Hangman)
# Alden Dent
# 9/21/21

from random import randint

head =    "   0"
noArms =  "   |"
oneArm =  "  \|"
twoArms = "  \|/"
torso =   "   |"
oneLeg =  "  /"
twoLegs = "  / \ "

def drawHangman(lives):
    print("---┐")
    if lives == 7:
        print("")
        print("")
        print("")
        print("")
    if lives == 6:
        print(head)
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


while True:
    word = input("Player 1, enter your word")
    print("\n" * 50)
    missedLetters = ""
    lives = 7
    guess = len(word)*"-"
    correctGuesses = 0
    wrongGuesses = 0
    hintsUsed = 0

    drawHangman(lives)
    print("Missed Letters: " + missedLetters)
    print(guess)
    
    while lives > 0 and guess != word:
        goodGuess = False
        guessedLetter = input("Guess a letter")
        if guessedLetter not in missedLetters and guessedLetter not in guess and len(guessedLetter) == 1 and guessedLetter.islower():
            for place in range(len(word)):
                if word[place] == guessedLetter:
                    guess = guess[:place] + guessedLetter + guess[place+1:]
                    goodGuess = True
                    correctGuesses = correctGuesses + 1
            if goodGuess == False:
                missedLetters = missedLetters + " " + guessedLetter
                lives = lives - 1
                wrongGuesses = wrongGuesses + 1
            drawHangman(lives)
            print("Missed Letters: " + missedLetters)
            print(guess)
        elif guessedLetter in missedLetters or guessedLetter in guess :
            print("That letter has already been guessed. Try again.")
        elif guessedLetter == "hint":
            place = randint(0, len(word)-1)
            guess = guess[:place] + word[place] + guess[place+1:]
            hintsUsed = hintsUsed + 1
            drawHangman(lives)
            print("Missed Letters: " + missedLetters)
            print(guess)
        elif len(guessedLetter) != 1:
            print("Do not enter multiple letters. Try again.")
        elif not guessedLetter.islower():
            print("Input must be a letter. Try again.")

    if(lives == 0):
        drawHangman(lives)
        print("You ran out of guesses!")
    else:
        print("You correctly guessed the word " + word)
    print(f"After {wrongGuesses} missed guesses, {correctGuesses} correct guesses, and {hintsUsed} hints used, the word was \"{word}\" ")
    if input("Do you want to play again? (y/n) ") == "n":
        break
