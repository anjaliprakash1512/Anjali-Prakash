# Write a python program that calculates the factorial of a given number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Prompt
number = int(input("Enter a number: "))

# Calculate
result = factorial(number)

print(f"The factorial of {number} is {result}")