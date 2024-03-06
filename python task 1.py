def fibonacci_generator(limit):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Yield the first two Fibonacci numbers
    yield a
    yield b
    
    # Generate Fibonacci numbers up to the limit
    while True:
        # Calculate the next Fibonacci number
        c = a + b
        # Check if the next Fibonacci number exceeds the limit
        if c > limit:
            break
        # Yield the next Fibonacci number
        yield c
        # Update the values of a and b for the next iteration
        a, b = b, c

# Test the fibonacci_generator function
limit = int(input("Enter the limit for Fibonacci series: "))
print("Fibonacci series up to", limit, ":")
for num in fibonacci_generator(limit):
    print(num, end=" ")
