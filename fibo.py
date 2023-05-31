def fibonacci(n):
    fib_seq = [0, 1] 
    
    while len(fib_seq) < n:
        next_num = fib_seq[-1] + fib_seq[-2]  
        fib_seq.append(next_num)  
    return fib_seq

sequence_length = 10
fib_numbers = fibonacci(sequence_length)
print(fib_numbers)