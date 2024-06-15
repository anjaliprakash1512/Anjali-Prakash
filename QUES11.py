#Write a python program that generates the first n numbers in the Fibonacci sequence.
# Function to generate the first n Fibonacci numbers
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

# Prompt the user to enter the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate the Fibonacci sequence
fibonacci_sequence = generate_fibonacci(n)

# Print the Fibonacci sequence
print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_sequence}")
