def fibonacci_generator(limit):
    # Initialize the first two Fibonacci numbers
    n1, n2 = 0, 1
    
    # Yield the first two Fibonacci numbers
    yield n1
    yield n2
    
    # Generate Fibonacci numbers up to the limit
    while True:
        # Calculate the next Fibonacci number
        FibNum = n1 + n2
        # Check if the next Fibonacci number exceeds the limit
        if FibNum > limit:
            break
        # Yield the next Fibonacci number
        yield FibNum
        # Update the values of a and b for the next iteration
        n1, n2 = n2, FibNum

# Test the fibonacci_generator function
limit = int(input("Enter the limit for Fibonacci series: "))
print("Fibonacci series up to", limit, ":")
for num in fibonacci_generator(limit):
    print(num, end=" ")
