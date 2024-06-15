#Write a python program that returns the minimum and maximum values in a list of numbers.
# Function to return the minimum and maximum values in a list of numbers
def find_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

# Prompt the user to enter a list of numbers separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the user input to a list of numbers
numbers_list = [float(num) for num in user_input.split()]

# Find the minimum and maximum values in the list
min_value, max_value = find_min_max(numbers_list)

# Print the minimum and maximum values
print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
