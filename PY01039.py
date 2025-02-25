

def check(n):
    if len(n) < 2:
        return "NO"
    
    check1 = set(n)

    if len(check1) != 2:
        return "NO"
    
    for i in range(len(n) - 2):
        if n[i] != n[i+2]:
            return "NO"
    return "YES"

for t in range(int(input())):
    n = input()
    print(check(n))

