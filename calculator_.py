# importmath 

import math


print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE ROOT")
print("6. RAISE TO POWER")

operation = input()

if operation == "1": #ADDITION
   num1 = input("Enter first number: ")
   num2 = input("Enter second number: ")
   print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2": #SUBTRACTION
   num1 = input("Enter first number: ")
   num2 = input("Enter second number: ")
   print("The sum is " + str(int(num1) - int(num2)))
elif operation == "3": #MULTIPLICATION
   num1 = input("Enter first number: ")
   num2 = input("Enter second number: ")
   print("The sum is " + str(int(num1) * int(num2)))
elif operation == "4": #DIVISION
   num1 = input("Enter first number: ")
   num2 = input("Enter second number: ")
   print("The sum is " + str(int(num1) / int(num2)))
elif operation == "5": #SQUARE ROOT
   num = int(input("Enter number: "))
   print("The squareroot is %f " %(math.sqrt(num)) )
elif operation == "6": #RAISE TO POWER
   num = int(input("Enter number: "))
   print("The result is %d " %(pow(num, 2)))
else: 
    print("Invalid Entry")
 