import math

def check(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

n , m = [int(i) for i in input().split()]
for i in range(n):
    list = [check(int(i)) for i in input().split()]
    print(*list)