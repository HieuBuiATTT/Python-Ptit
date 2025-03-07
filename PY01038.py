def dao_nguoc(n):
    return int(str(n)[::-1])


def qua_trinh():
    for t in range(int(input())):
        n = int(input())
        for _ in range(1000):
            if n % 7 == 0:
                print(n)
                break
            n += dao_nguoc(n)
        else:
            print(-1)

qua_trinh()

