n = int(input())
matran = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

upper_sum = sum(matran[i][j] for i in range(n) for j in range(i+1,n))
lower_sum = sum(matran[i][j] for i in range(1,n) for j in range(i))

chenhlech = abs(upper_sum  - lower_sum)

print("YES" if chenhlech <= k else "NO")

print(chenhlech)

