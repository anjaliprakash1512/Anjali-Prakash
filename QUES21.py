#Write a python program that counts the occurrences of a specific element in a list.
# Function to count occurrences of a specific element in a list
def count_occurrences(lst, element):
    return lst.count(element)

# Prompt the user to enter the list of elements separated by spaces
user_input = input("Enter a list of elements separated by spaces: ")

# Convert the user input to a list of elements
elements_list = user_input.split()

# Prompt the user to enter the element to count
element_to_count = input("Enter the element to count: ")

# Count the occurrences of the specified element
occurrences = count_occurrences(elements_list, element_to_count)

# Print the count
print(f"The element '{element_to_count}' occurs {occurrences} times in the list.")
