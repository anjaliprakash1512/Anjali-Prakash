#Write a python program that checks if two strings are anagrams of each other.
# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Clean the strings by removing spaces and converting to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the characters in each string and compare
    return sorted(str1) == sorted(str2)


# Prompt the user to enter the first string
string1 = input("Enter the first string: ")

# Prompt the user to enter the second string
string2 = input("Enter the second string: ")

# Check if the strings are anagrams
if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' are not anagrams.")
