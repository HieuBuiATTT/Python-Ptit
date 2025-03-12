def nguyento(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = all(num % p != 0 for p in primes)
        if is_prime:
            primes.append(num)
        num += 1
    return primes

def check(n,x):
    primes = nguyento(n)
    sequence = [x]
    for p in primes:
        x += p
        sequence.append(x)
    return sequence


n, x = map(int, input().split())


result = check(n, x)
print(" ".join(map(str, result)))