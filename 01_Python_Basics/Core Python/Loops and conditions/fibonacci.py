def fibonacci_iterative(n):
    """Return the first n Fibonacci numbers using a loop."""
    if n <= 0:
        return []
    sequence = [0]
    if n == 1:
        return sequence

    sequence.append(1)
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def fibonacci_recursive(n):
    """Return the nth Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative index")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_generator(limit):
    """Yield Fibonacci numbers up to a maximum value."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    count = 10
    print("First 10 Fibonacci numbers:", fibonacci_iterative(count))
    print("Fibonacci number at index 7:", fibonacci_recursive(7))

    print("Fibonacci numbers up to 50:")
    for value in fibonacci_generator(50):
        print(value, end=" ")
    print()
