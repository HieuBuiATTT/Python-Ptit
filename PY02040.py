
def check(n, matran, k):
    upper_sum = 0
    lower_sum = 0

    for i in range(n):
        for j in range(n):
            if j > n - i - 1:
                upper_sum += matran[i][j]
            elif j < n - i - 1:
                lower_sum += matran[i][j]
    
    diff = abs(upper_sum - lower_sum)

    if diff <= k:
        print("YES")
    else:
        print("NO")
    print(diff)


n = int(input())
matran = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

check(n,matran,k)
