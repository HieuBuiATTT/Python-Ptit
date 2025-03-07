from itertools import permutations

s = input().split()

hoan_vi = sorted(permutations(s))

for hv in hoan_vi:
    print("".join(hv))