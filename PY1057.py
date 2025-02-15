import math

def nguyento(s):
    for i in range(2,int(math.sqrt(s)) + 1):
        if s % i == 0:
            return 0
    return s > 1

def check(s):
    for i in range(len(s)):
        if(nguyento(i) and not nguyento(int(s[i])) or not nguyento(i) and nguyento(int(s[i]))):
            return 'NO'
    return 'YES'
for t in range(int(input())):
    s = input()
    print(check(s))
