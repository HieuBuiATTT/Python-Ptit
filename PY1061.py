
import math

def check(s):
    for i in range(2,int(math.sqrt(s)) + 1):
        if s % i == 0:
            return 0
    return s > 1

for t in range(int(input())):
    s = input()
    a = int(s[0:3])
    b = int(s[-3:])
    print("YES" if len(s) >=4 and check(a) and check(b) else "NO")
    
