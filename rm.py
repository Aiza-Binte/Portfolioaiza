# Calculator program
# Ask the user for the first number
num1 = input("Enter the first number: ")
# Ask the user for the operator
operator = input("Enter the operator (+, -, *, /): ")
# Ask the user for the second number
num2 = input("Enter the second number: ")
# Covert the input from text to a number
num1 = float(num1)
num2 = float(num2)
#Check which operator is chosen
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2   
else:
    print("Invalid operator!")
# show the result
print(f"The result is: {result}")