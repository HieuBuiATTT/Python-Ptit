
def check(s,n):
    return s.count(n)


for t in range(int(input())):
    s = input().strip()
    n = input().strip()
    print(check(s,n))

