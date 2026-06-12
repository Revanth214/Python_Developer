def is_prime(n):
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_list(limit):
    """Return a list of prime numbers up to the given limit."""
    if limit < 2:
        return []
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes


if __name__ == "__main__":
    test_number = 29
    print(f"Is {test_number} prime?", is_prime(test_number))
    print("Primes up to 50:", prime_list(50))
