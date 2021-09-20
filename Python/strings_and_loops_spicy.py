# Python Program 03 - Strings and Loops Spicy Version
# Alden Dent
# 9/20/21

# Since the spicy version is to condense the program into the fewest amount of lines,
# this code is quite hard to read
# input("input").replace(" ", "-") + "-" takes the user's input, replaces each space with -
# and adds another - at the end so there is one at the end of every word
# print(character) for character in input() iterates through each character of the string
# and prints that character

[print(character) for character in input("Type in your text, then press Enter:").replace(" ", "-") + "-"]
