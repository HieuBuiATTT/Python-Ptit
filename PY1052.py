import math

def check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True if n > 1 else False

for t in range(int(input())):
    s = input()
    n = sum(int(i) for i in s)
    print("YES" if check(n) else "NO")

