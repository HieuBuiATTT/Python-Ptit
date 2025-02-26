
def check(n):
    dem = 0
    if len(n) == 1:
        dem = 1
        return dem 
    while len(n) > 1:
        n = str(sum(ord(digit) -48 for digit in n))
        dem += 1
    return dem

n = input().strip()
print(check(n))