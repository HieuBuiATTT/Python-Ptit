for t in range(int(input())):
    s = input()
    n = sum(int(i) for i in s)
    print("YES" if n % 3 == 0 else "NO")
