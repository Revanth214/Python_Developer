def factorial_iterative(n):
    """Return n! using a loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Return n! using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    number = 5
    print(f"Iterative factorial of {number} is {factorial_iterative(number)}")
    print(f"Recursive factorial of {number} is {factorial_recursive(number)}")
