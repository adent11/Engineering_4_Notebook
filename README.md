# Engineering_4_Notebook

## Table of Contents

* [Python_Calculator](#Python_Calculator)
---


## Python_Calculator

### Assignment Description

In this assignment I made a function that allows you to do addition, subtraction, multiplication, division, and remainder division. It takes three values as parameters, two numbers to do the operations with and a third value that determines which operation will be done on the other values. The spicy version added the ability to do factorials, which returns a list that includes the factorials of both numbers instead of just one number like the other operations.

### Evidence 

<details><summary><b>Vanilla Version</b></summary>

``` python
# Python Program 01 - Calculator
# Alden Dent
# 9/14/21

SUM_CONSTANT = 1            #These constants make it easier and more readable
DIFFERENCE_CONSTANT = 2     #to pass the operation to the function 
PRODUCT_CONSTANT = 3
QUOTIENT_CONSTANT = 4
MODULO_CONSTANT = 5

def doMath(num1, num2, operation):
    if operation == SUM_CONSTANT:
        return num1 + num2
    if operation == DIFFERENCE_CONSTANT:
        return num1 - num2
    if operation == PRODUCT_CONSTANT:
        return num1 * num2
    if operation == QUOTIENT_CONSTANT:
        return round(num1 / num2, 2)
    if operation == MODULO_CONSTANT:
        return num1 % num2

print("CALCULATOR PROGRAM")
a = int(input("Enter your first number: "))  #Sets each value to the number input by the user
b = int(input("Enter your second number: "))

print("Sum:\t\t" + str(doMath(a,b,SUM_CONSTANT)))               #Does each function for the input values
print("Difference:\t" + str(doMath(a,b,DIFFERENCE_CONSTANT)))
print("Product:\t" + str(doMath(a,b,PRODUCT_CONSTANT)))
print("Quotient:\t" + str(doMath(a,b,QUOTIENT_CONSTANT)))
print("Modulo:\t\t" + str(doMath(a,b,MODULO_CONSTANT)))
```

</details>

<details><summary><b>Spicy Version</b></summary>
  
``` python
# Python Program 01 - Calculator Spicy Version
# Alden Dent
# 9/14/21

SUM_CONSTANT = 1            #These constants make it easier and more readable
DIFFERENCE_CONSTANT = 2     #to pass the operation to the function 
PRODUCT_CONSTANT = 3
QUOTIENT_CONSTANT = 4
MODULO_CONSTANT = 5
FACTORIAL_CONSTANT = 6

def doMath(num1, num2, operation):
    if operation == SUM_CONSTANT: #All of these check the operation passed to the function and return that operation of a and b
        return num1 + num2
    if operation == DIFFERENCE_CONSTANT:
        return num1 - num2
    if operation == PRODUCT_CONSTANT:
        return num1 * num2
    if operation == QUOTIENT_CONSTANT:
        return round(num1 / num2, 2)
    if operation == MODULO_CONSTANT:
        return num1 % num2
    if operation == FACTORIAL_CONSTANT:
        aFact = 1 #Stores the factorial of a
        bFact = 1 #Stores the factorial of b
        for x in range(1, a+1): #This for loop calculates the factorial of a
            aFact = aFact * x
        for x in range(1, b+1): #This for loop calculates the factorial of b
            bFact = bFact * x
        return [aFact, bFact] #This returns a list with the factorial of both a and b

print("CALCULATOR PROGRAM")
a = int(input("Enter your first number: "))  #Sets each value to the number input by the user
b = int(input("Enter your second number: "))

print("Sum:\t\t" + str(doMath(a,b,SUM_CONSTANT)))               #Does each operation for the input values
print("Difference:\t" + str(doMath(a,b,DIFFERENCE_CONSTANT)))
print("Product:\t" + str(doMath(a,b,PRODUCT_CONSTANT)))
print("Quotient:\t" + str(doMath(a,b,QUOTIENT_CONSTANT)))
print("Modulo:\t\t" + str(doMath(a,b,MODULO_CONSTANT)))
print("1st Factorial:\t" + str(doMath(a,b,FACTORIAL_CONSTANT)[0])) #Displays only the first item on the list, which is the factorial of a
print("2nd Factorial:\t" + str(doMath(a,b,FACTORIAL_CONSTANT)[1])) # Displays only the second item on the list, which is the factorial of b
```

</details>

### Reflection

This assignment was relatively simple, but still had many valuable lessons. Since it has been a while since I have coded in Python, reference websites like <https://www.w3schools.com/python> are very helpful for remembering syntax and giving simple descriptions and examples of how different parts of Python work. I also learned that you can return a list from a function and access the different items using ``` functionName(parameters)[itemNumber] ```.
