def fibonacci(limit):
    """Generate Fibonacci numbers."""
    n1, n2 = 0, 1
    while n1 <= limit:
        yield n1
        n1, n2 = n2, n1 + n2
fibs = fibonacci(100)
for fib in fibs:
    print(fib)