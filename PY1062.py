
import math

def nguyento(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

for t in range(int(input())):
    s = input()
    n = int(len(s))
    dem = 0
    for i in range(len(s)):
        if nguyento(int(s[i])):
            dem += 1
    print("YES" if dem > len(s) - dem and nguyento(n) else "NO")


