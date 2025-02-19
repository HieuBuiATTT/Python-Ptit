def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def slove():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        arr.sort(key=lambda x: (digit_sum(x), x))
        print(*arr)

if __name__ == "__main__":
    slove()

