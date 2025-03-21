def kiem_tra_thang_bang(xau):
    do_dai = len(xau)
    xau_dao = xau[::-1]

    for i in range(1, do_dai):
        if  abs(ord(xau[i]) - ord(xau[i-1])) != abs(ord(xau_dao[i]) - ord(xau_dao[i-1])):
            return "NO"
    return "YES"


for _ in range(int(input())):
    xau_ki_tu = input().strip()
    print(kiem_tra_thang_bang(xau_ki_tu))
