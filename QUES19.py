#Write a python program that removes all punctuation from a given string.
import string

# Function to remove all punctuation from a given string
def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    # Translate the input string using the translation table
    return input_string.translate(translator)

# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Remove punctuation from the string
clean_string = remove_punctuation(user_input)

# Print the string without punctuation
print(f"The string without punctuation is: {clean_string}")
