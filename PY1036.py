for t in range(int(input())):
    n = int(input())
    dem = 0.0
    if n % 2 == 0:
        for i in range(2,n+2,2):
            dem += 1/i
    else:
        for i in range(1,n+2,2):
            dem += 1/i
    print('{:.6f}'.format(dem))        