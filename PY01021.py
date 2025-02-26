
def check(n):
    letters = []
    dem = 0

    for char in n:
        if char.isdigit():
            dem += int(char)
        else:
            letters.append(char)
    letters.sort()

    ketqua = "".join(letters)
    if dem > 0:
        ketqua += str(dem)
    return ketqua


for t in range(int(input())):
    n = input().strip()
    print(check(n))

