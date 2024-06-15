#Write a program in python that counts the frequency of each character in a string.
# Function to count the frequency of each character in a string
def count_char_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Prompt
user_input = input("Enter a string: ")

# Calculate the character frequency
char_frequency = count_char_frequency(user_input)

# Print the character frequencies
print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")
