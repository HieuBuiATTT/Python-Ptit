def check(n):
    while len(n) > 1:
        mid = len(n) // 2
        dau = int(n[:mid])
        sau = int(n[mid:])
        ketqua = dau + sau
        print(ketqua)
        ketqua = str(ketqua)

n = input().strip()
check(n)