#Write a program that acts as a simple calculator. It should take twonumbers and an operator (+, -, *, /) as input and print the result.
# Function to perform the chosen operation
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"

# Prompt the user to enter the first number
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = float(input("Enter the second number: "))

# Prompt the user to enter an operator
operator = input("Enter an operator (+, -, *, /): ")

# Perform the calculation
result = calculate(num1, num2, operator)

# Print the result
print(f"The result of {num1} {operator} {num2} is: {result}")
