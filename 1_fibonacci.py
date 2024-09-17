def fibonacci_sequence(n):
    # Initializes the first two numbers of the Fibonacci sequence
    fib_seq = [0, 1]

    # Calculates the sequence until the last value is greater than or equal to the number entered
    while fib_seq[-1] < n:
        next_value = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_value)

    # Checks if the number entered belongs to the sequence
    if n in fib_seq:
        return f"The number {n} belongs to the Fibonacci sequence."
    else:
        return f"The number {n} does not belong to the Fibonacci sequence."

# Requests user input
number = int(input("Enter a number: "))

# Display the result
print(fibonacci_sequence(number))
