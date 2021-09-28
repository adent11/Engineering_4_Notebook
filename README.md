# Engineering_4_Notebook

## Table of Contents

* [Python_Calculator](#Python_Calculator)
* [Python_Quadratic_Solver](#Python_Quadratic_Solver)
* [Python_Strings_and_Loops](#Python_Strings_and_Loops)
* [Python_MSP](#Python_MSP) (Hangman)
---


## Python_Calculator

### Assignment Description

In this assignment, I made a function that allows you to do addition, subtraction, multiplication, division, and remainder division. It takes three values as parameters, two numbers to do the operations with and a third value that determines which operation will be done on the other values. The spicy version added the ability to do factorials, which returns a list that includes the factorials of both numbers instead of just one number like the other operations.

### Evidence 

<details><summary><b>Vanilla Version</b></summary><br/>

[Calculator Vanilla Version Code](https://github.com/adent11/Engineering_4_Notebook/blob/main/Python/calculator.py)<br/><br/>
Program Output:<br/>
<IMG SRC="Media/PythonCalculator.png" width="250" height="240"> <br/>

<br/></details>

<details><summary><b>Spicy Version</b></summary><br/>
 
[Calculator Spicy Version Code](https://github.com/adent11/Engineering_4_Notebook/blob/main/Python/calculator_spicy.py)<br/><br/>
Program Output:<br/>
<IMG SRC="Media/PythonCalculatorSpicy.png" width="250" height="293"> <br/>
<br/></details>

### Reflection

This assignment was relatively simple, but still had many valuable lessons. Since it has been a while since I have coded in Python, reference websites like <https://www.w3schools.com/python> are very helpful for remembering syntax and giving simple descriptions and examples of how different parts of Python work. I also learned that you can return a list from a function and access the different items using ``` functionName(parameters)[itemNumber] ```.

 
## Python_Quadratic_Solver

### Assignment Description

In this assignment, I wrote a program that takes a, b, and c, of a quadratic equation in the form y = ax^2+bx+c, and returns the roots of the function, or a message stating that they don't exist if they are imaginary. I divided each of these tasks into different functions, one to calculate and return the discriminant, which tells you if there are real roots, another to find and return the roots. It then asks for a new set of a, b, and c, or for the user to end the program. For the spicy version, I made it print out the equation with the inputted a, b, and c plugged in, and added another function which puts the equation in vertex form.
 
### Evidence

<details><summary><b>Vanilla Version</b></summary><br/>

[Quadratic Solver Vanilla Version Code](https://github.com/adent11/Engineering_4_Notebook/blob/main/Python/quadratic_solver.py)<br/><br/>
Program Output:<br/>
<IMG SRC="Media/PythonQuadraticSolver.png" width="250" height="251"> <br/>

<br/></details>
 
<details><summary><b>Spicy Version</b></summary><br/>

[Quadratic Solver Spicy Version Code](https://github.com/adent11/Engineering_4_Notebook/blob/main/Python/quadratic_solver_spicy.py)<br/><br/>
Program Output:<br/>
<IMG SRC="Media/PythonQuadraticSolverSpicy.png" width="250" height="290"> <br/>

<br/></details>
 
### Reflection

This assignment taught me the syntax for squaring things in Python, ``` a ** x ```, as well as how to import and use the square root function, ``` from math import sqrt ``` and ``` sqrt(x) ```. I also learned how to use f strings to be able to put variables inside of strings more easily, <br/> ``` f" This is {variableA} and {variableB}" ```.

 
## Python_Strings_and_Loops

### Assignment Description

In this assignment, I wrote a program that takes a sentence input by the user and prints out each character on a new line, with a - after each word. For the spicy version, I condensed the whole program into one line of code, while retaining the same functionality.

### Evidence
 
<details><summary><b>Vanilla Version</b></summary><br/>

[Strings and Lists Vanilla Version Code](https://github.com/adent11/Engineering_4_Notebook/blob/main/Python/strings_and_lists.py)<br/><br/>
Program Output:<br/>
<IMG SRC="Media/PythonStringsAndLists.png" width="250" height="318"> <br/>

<br/></details>
 
<details><summary><b>Spicy Version</b></summary><br/>

[Strings and Lists Spicy Version Code](https://github.com/adent11/Engineering_4_Notebook/blob/main/Python/strings_and_lists_spicy.py)<br/><br/>
Program Output:<br/>
<IMG SRC="Media/PythonStringsAndLists.png" width="250" height="318"> <br/>

<br/></details>
 
### Reflection

In this assignment I learned a few things, but didn't run in to any major obstacles. While doing the vanilla version, I learned that in Python, you can use ```list(string)``` to create a list with each character in the string as its own element and ```string.split()``` to create a list of each substring in the string between a certain character, which defaults to a space. In the spicy version, I learned a new string method (you can replace every instance of a certain character in a string with another character using ```string.replace(oldCharacter, newCharacter)```), but my main takeaway that Python for loop syntax can be very strange; you can put a print statement on the same line before the for statement it is printing the value of, but only if you have brackets around it. (I think, at least, although I have no idea why this syntax would be used)
 
 ## Python_MSP
 
 ### Assignment Description
 In this assignment, the goal was to create a hangman game. One user enters the word, then another guesses letter until they have either guessed all letters correctly or they run out of lives. For each correct guess, that letter is added to the guess, while for each incorrect guess, a body part is added to the hangman and a life is subtracted. For the spicy version, I added a list of incorrect guesses, exceptions for if the letter entered had already been guessed or was not a single, lower case letter, a hint system, and a counter for correct guesses, incorrect guesses, and hints used.
 
 
 ### Proof
 
 ### Reflection
