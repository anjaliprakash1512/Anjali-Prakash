#Write a python program that calculates the sum of the digits of a given number.
# Function 
def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number = number // 10
    return sum_digits

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Calculate the sum of the digits
result = sum_of_digits(number)

# Print the result
print(f"The sum of the digits of {number} is {result}")
