#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
# Initialize an empty list to store the lines
lines = []

# Read lines of input from the user until an empty line is entered
while True:
    line = input("Enter a line (or press Enter to finish): ")
    if line:
        lines.append(line)
    else:
        break

# Print all the lines
print("The lines you entered are:")
for line in lines:
    print(line)
