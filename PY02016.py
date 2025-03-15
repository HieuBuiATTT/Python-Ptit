from collections import Counter

t = int(input())

for _ in range(t):

    n = int(input())

    a = list(map(int, input().split()))

    count = Counter(a)

    ketqua = "NO"

    for so, tansuat in count.items():
        if tansuat > n/2:
            if ketqua == "NO" or so < ketqua:
                ketqua = so
    

    print(ketqua)


