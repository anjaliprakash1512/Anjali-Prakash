#Write a program in python that converts a string into a list of its characters.
# Function to convert a string into a list of its characters
def string_to_list(input_string):
    return list(input_string)

# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Convert the string to a list of characters
characters_list = string_to_list(input_string)

# Print the list of characters
print("The list of characters is:", characters_list)
