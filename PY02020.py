n = int(input())

a = list(map(float, input().split()))

a = sorted(set(a))

if len(a) >= 1:
    dem = sum(a[1:-1])/len(a[1:-1])

print(f"{dem:.2f}")

