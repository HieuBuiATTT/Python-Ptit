from itertools import combinations

def check(n,k,a):
    lay_phan_tu = sorted(set(a))
    ket_qua = combinations(lay_phan_tu, k)

    for comb in ket_qua:
        print(" ".join(map(str, comb)))


n,k = map(int, input().split())

a = list(map(int, input().split()))

check(n,k,a)

