def fibonacci(n):
    fib_seq = [0, 1]  # Initialize the sequence with the first two numbers
    
    # Generate the Fibonacci sequence up to the desired length
    while len(fib_seq) < n:
        next_num = fib_seq[-1] + fib_seq[-2]  # Compute the next number in the sequence
        fib_seq.append(next_num)  # Add the next number to the sequence
        
    return fib_seq

# Example usage
sequence_length = 10
fib_numbers = fibonacci(sequence_length)
print(fib_numbers)