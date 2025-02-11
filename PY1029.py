
import math

for t in range(int(input())):
    n = int(input())
    dao = int(str(n)[::-1])
    check = math.gcd(n,dao)
    if check == 1:
        print("YES")
    else:
        print("NO")