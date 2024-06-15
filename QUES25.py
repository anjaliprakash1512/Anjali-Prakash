# Write a program that copies the contents of one text file to another.
# Function to copy contents from one file to another
def copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode and destination file in write mode
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            # Read the contents of the source file
            contents = source.read()
            # Write the contents to the destination file
            destination.write(contents)
        print("File copied successfully!")
    except FileNotFoundError:
        print("One of the files does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user to enter the source file name
source_file_name = input("Enter the source file name: ")

# Prompt the user to enter the destination file name
destination_file_name = input("Enter the destination file name: ")

# Copy the contents from the source file to the destination file
copy_file(source_file_name, destination_file_name)
