number1= input("Enter the first number")
if not number1.isdigit():
    number1 = input("Wrong input try again")

number2= input("Enter the second number")
if not number2.isdigit():
    number2= input("Wrong input try again")

operation= input("Choose the operation") 

number1= int(number1)
number2= int(number2)

answer="invalid"
if operation == '+':
    answer= number1 + number2

elif operation == '-':
   answer= number1 - number2

elif operation == '/':
    answer= number1/number2

elif operation == '*':
    answer= number1*number2
else:
    print("Invalid input")

print("The answer is %s" % (answer))









