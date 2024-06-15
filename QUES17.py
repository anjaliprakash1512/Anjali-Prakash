#Write a program in python that converts a given string to title case (first letter of each word capitalized).
# Function to convert a string to title case
def to_title_case(input_string):
    return input_string.title()

# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Convert the string to title case
title_case_string = to_title_case(user_input)

# Print the title case string
print(f"The string in title case is: {title_case_string}")
