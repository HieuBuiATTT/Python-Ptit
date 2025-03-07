def dem_cap_khac_nhau(so_phan_tu, day_so):
    dem = 0

    for i in range(so_phan_tu - 1):
        if day_so[i] != day_so[i+1]:
            dem += 1
    return dem


so_phan_tu = int(input())

day_so = list(map(int, input().split()))

print(dem_cap_khac_nhau(so_phan_tu, day_so))

