import sys

def product_of_digits(n):
    prod = 1
    for digit in str(n):
        if digit != '0':
            prod *= int(digit)
    return prod

def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        
        arr.sort(key=lambda x: (product_of_digits(x), x))
        print(" ".join(map(str, arr)))

if __name__ == "__main__":
    solve()
