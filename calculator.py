SUM_CONSTANT = 1            #These contstants make it easier and more readable
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
        return num1 / num2
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
