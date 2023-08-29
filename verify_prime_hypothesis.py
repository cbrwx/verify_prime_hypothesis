# Testing the hypothesis that for all prime numbers greater than 5, p^2 - 1 is a multiple of 24.

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testing the hypothesis for prime numbers up to 1000
test_results = []
for p in range(6, 1001):  # Starting from 6 because we're considering primes greater than 5
    if is_prime(p):
        test_results.append((p**2 - 1) % 24 == 0)

# If the hypothesis is correct, all elements in test_results should be True
all(test_results)
