num1 = float(input("Enter a num 1 "))
num2= float(input("Enter a num 2 "))

print(" choose operations : + - * / ")

operation = input("Enter the operation : ")

if(operation == "+"):
    result = num1 + num2
elif(operation == "-"):
    result = num1 - num2
elif(operation == "*"):
    result = num1 * num2 
elif(operation == "/"):
   if num2 != 0:
       result = num1 / num2
   else:
     result = "Error ! Divison by zero."

else:
    invalid = "Invalid operation!"

print(" Result: " ,result)
