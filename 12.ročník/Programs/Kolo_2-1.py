lines = open("../input.txt").read().splitlines()
output = open("../Solution.txt", "w")


def prime_check(n: int) -> bool:
    global primes
    threshold = int(n**(1/2))
    for prime in primes[1:]:
        if prime > threshold:
            return True
        if not n % prime:
            return False
    return True


def get_index(num: int) -> int:
    if num > primes[-1]:
        for n in range(primes[-1]+1, num+1):
            if prime_check(n):
                primes.append(n)
        return len(primes)-1
    elif num < primes[-1]:
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
    else:
        return len(primes)-1


primes = [1]
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
