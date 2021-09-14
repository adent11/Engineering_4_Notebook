SUM_CONSTANT = 1            #These contstants make it easier and more readable
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
        return num1 / num2
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
