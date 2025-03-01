def check(n,d,a):
    d = d % n
    return a[d:] + a[:d]

for t in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    print(*check(n,d,a))

