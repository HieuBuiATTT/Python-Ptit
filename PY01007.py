import sys
import math

def check(n,x,m):
    nam = math.log(m/n)/math.log(1+x/100)
    return math.ceil(nam)

for t in range(int(input())):
    n,x,m = map(float, input().split())
    print(check(n,x,m))

    