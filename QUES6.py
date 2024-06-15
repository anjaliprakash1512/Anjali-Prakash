#Write a program that reads the content of a text file and prints it to the Console.
# Specify the file name
file_name = "ques_5.txt"

# Open the file in read mode and read the content
try:
    with open(file_name, "r") as file:
        content = file.read()
        print("The content of the file is:")
        print(content)
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
