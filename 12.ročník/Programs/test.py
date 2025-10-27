def sieve_of_eratosthenes(limit):
    # Create a boolean array "is_prime[0..limit]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Start with the first prime number, 2
    p = 2
    while (p * p <= limit):
        # If is_prime[p] is still true, then it is a prime
        if is_prime[p]:
            # Update all multiples of p
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1

    # Collect all prime numbers
    primes = [i for i, prime_status in enumerate(is_prime) if prime_status]
    return primes

# Generate primes up to 1,000,000
limit = 1000000
prime_numbers = sieve_of_eratosthenes(limit)

print(prime_numbers)
# You can now use the 'prime_numbers' list
# print(prime_numbers[:10]) # Print the first 10 primes
# print(len(prime_numbers)) # Print the count of primes