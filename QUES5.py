#Write a program that takes a string input from the user and writes it to a text file.
# Prompt
user_input = input("Enter a string to write to the file: ")

# Specify the file name
file_name = "Ques_5.txt"

# Open the file in write mode and write the user input to the file
with open(file_name, "w") as file:
    file.write(user_input)

# Print a confirmation message
print(f"The string has been written to {file_name}.")
