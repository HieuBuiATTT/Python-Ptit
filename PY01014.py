a,k,n = map(int, input().split())
if a + k >= n:
    print(-1)
else:
    for i in range(k - a%k, n + 1 - a, k):
        print(i,end=' ')