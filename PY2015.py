
def check(a):
    dem = 0
    while len(set(a)) > 1:
        a = [abs(a[i] - a[(i+1) % 4]) for i in range(4)]
        dem += 1
    return dem 


while True:
    a = list(map(int,input().split()))
    if a == [0,0,0,0]:
        break
    print(check(a))