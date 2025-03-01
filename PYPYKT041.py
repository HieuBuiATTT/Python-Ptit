
def check(luoi, n):

    tong_so_cap = 0
    for hang in luoi:
        so_dong_xu = hang.count('C')
        tong_so_cap += (so_dong_xu*(so_dong_xu - 1)) // 2
    for cot in range(n):
        so_dong_xu = sum(1 for hang in luoi if hang[cot] == 'C')
        tong_so_cap += (so_dong_xu*(so_dong_xu-1)) // 2
    
    return tong_so_cap



n = int(input())
luoi =  [input().strip() for _ in range(n)]

print(check(luoi, n))


