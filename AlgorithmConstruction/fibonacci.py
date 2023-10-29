def generate_fibonacci(n):
    # Initialize the list to store the Fibonacci numbers
    fibonacci_sequence = []

    # First two Fibonacci numbers
    a, b = 0, 1

    # Ensure n is a non-negative integer
    if n <= 0:
        return []

    # Add the first two numbers to the sequence
    if n >= 1:
        fibonacci_sequence.append(a)
    if n >= 2:
        fibonacci_sequence.append(b)

    # Generate the rest of the Fibonacci numbers
    for _ in range(2, n):
        a, b = b, a + b
        fibonacci_sequence.append(b)

    return fibonacci_sequence

n = 10  
fibonacci_numbers = generate_fibonacci(n)
print(fibonacci_numbers)
