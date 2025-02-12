import math

n,k = [int(i) for i in input().split()]
dau = 10**(k-1)
cuoi = 10**k
dem = 0
for i in range(dau, cuoi):
    if math.gcd(n,i) == 1 :
        print(i,end=' ')
        dem += 1
        if dem % 10 == 0:
            print()
