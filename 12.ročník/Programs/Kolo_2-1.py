lines = open("../input.txt").read().splitlines()
output = open("../Solution.txt", "w")


def get_index(num: int) -> int:
    s = 0
    e = len(primes)-1
    while s != e:
        m = (s+e)//2
        if num < primes[m]:
            e = m
        elif num > primes[m]:
            s = m+1
        else:
            return m
    return s-1


limit = 10**6+100
is_prime = [True]*(limit+1)
is_prime[0] = False
p = 2
while p*p <= limit:
    if is_prime[p]:
        for multiple in range(p*p, limit+1, p):
            is_prime[multiple] = False
    p += 1
primes = [i for i, prime_status in enumerate(is_prime) if prime_status]

for line in range(2, len(lines), 2):
    original_sequence = list(map(int, lines[line].split()))
    prime_sequence = []
    for num in original_sequence:
        prime_sequence.append(get_index(num))
    results = []
    length = len(original_sequence)
    for r in [range(length), range(length-1, -1, -1)]:
        steps = 0
        last = original_sequence[r[0]]
        last_prime = prime_sequence[r[0]]
        for i in r[1:]:
            current = original_sequence[i]
            current_prime = prime_sequence[i]
            if current > last:
                if current_prime > last_prime:
                    if current > primes[current_prime]:
                        steps += 1
                    steps += current_prime-last_prime
                    last = primes[last_prime]
                elif current_prime == last_prime:
                    steps += 1
                    last = primes[current_prime]
                else:
                    raise Exception
            else:
                last = current
                last_prime = current_prime
        results.append(steps)
    print(min(results), file=output)
