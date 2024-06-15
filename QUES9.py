#Write a python program that checks if a substring is present in a given string.
# Prompt
main_string = input("Enter the main string: ")

# Prompt 
substring = input("Enter the substring to check: ")

# Check if the substring is in the main string
if substring in main_string:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")
