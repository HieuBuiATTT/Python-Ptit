pheptoan = input().strip()

a, cong , b , bang, c = pheptoan.split()

a = int(a)
b = int(b)
c = int(c)

if a + b == c:
    print("YES")
else:
    print("NO")