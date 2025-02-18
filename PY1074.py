import sys

MAXN = 2_000_000
smallest_prime = [0] * (MAXN + 1)  

def sieve():
    for i in range(2, MAXN + 1):
        if smallest_prime[i] == 0:  
            for j in range(i, MAXN + 1, i):
                if smallest_prime[j] == 0:
                    smallest_prime[j] = i  

def phantichthuasonguyento(b):
    tong = 0
    while b > 1:
        tong += smallest_prime[b]
        b //= smallest_prime[b]
    return tong

# Đọc nhanh với sys.stdin.readline()
n = int(sys.stdin.readline().strip())
dem = 0
for _ in range(n):
    a = int(sys.stdin.readline().strip())
    dem += phantichthuasonguyento(a)

print(dem)
