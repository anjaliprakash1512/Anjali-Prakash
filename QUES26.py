#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
# Function to check if a string starts with a given prefix
def starts_with(string, prefix):
    return string.startswith(prefix)

# Function to check if a string ends with a given suffix
def ends_with(string, suffix):
    return string.endswith(suffix)

# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Prompt the user to enter a prefix to check
prefix = input("Enter a prefix to check: ")

# Prompt the user to enter a suffix to check
suffix = input("Enter a suffix to check: ")

# Check if the string starts with the given prefix
if starts_with(input_string, prefix):
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not start with the prefix '{prefix}'.")

# Check if the string ends with the given suffix
if ends_with(input_string, suffix):
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not end with the suffix '{suffix}'.")
