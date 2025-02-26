import sys

def check(n):
    i = 0 
    while i < len(n):
        if n[i] == '6':
            if i + 1 < len(n) and n[i+1] == '8':
                if i + 2 < len(n) and n[i+2] == '8':
                    i+=3
                else:
                    i+=2
            else:
                i+=1
        else:
            return "NO"
    return "YES"


n = input()
print(check(n))