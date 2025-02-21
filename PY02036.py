
from math import gcd
from itertools import combinations

def check(arr):
    arr.sort()
    pairs = [(a,b) for a, b in combinations(arr, 2) if gcd(a,b) == 1]
    return pairs

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    a = check(arr)

    for b, c in a:
        print(b, c) 

if __name__ == "__main__":
    main()