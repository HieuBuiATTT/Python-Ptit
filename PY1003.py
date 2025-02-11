import math

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    lamchon = 10


    while n >= lamchon:
        n = math.ceil(n/lamchon) * lamchon
        lamchon *= 10
    print(n)
