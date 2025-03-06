import math

def nguyento(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

def check(n,m, matran):
    ketqua = [[1 if nguyento(matran[i][j]) else 0 for j in range(m)] for i in range(n)]
    return ketqua


n, m = map(int, input().split())

matran = [list(map(int, input().split())) for _ in range(n)]

ketqua = check(n, m , matran)

for row in ketqua:
    print(" ".join(map(str, row)))



