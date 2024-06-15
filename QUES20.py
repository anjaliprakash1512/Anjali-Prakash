#Write a python program that takes a list of numbers and returns their sum.
# Function to calculate the sum of a list of numbers
def sum_of_list(numbers):
    return sum(numbers)

# Prompt the user to enter numbers separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the user input to a list of numbers
numbers_list = [float(num) for num in user_input.split()]

# Calculate the sum of the list
total_sum = sum_of_list(numbers_list)

# Print the sum
print(f"The sum of the numbers is: {total_sum}")

