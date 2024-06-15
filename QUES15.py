#Write a program that reads data from a CSV file and prints it to the console.
import csv

# Specify the CSV file name
csv_file = 'vgsales.csv'

# Open the CSV file in read mode
with open(csv_file, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Read and print each row in the CSV file
    for row in csv_reader:
        print(', '.join(row))
