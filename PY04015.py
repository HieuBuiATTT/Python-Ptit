

class KhachHang:
    def __init__(self, ma, ten, chi_so_cu, chi_so_moi):
        self.ma = f"KH{ma:02d}"
        self.ten = ten
        self.chi_so_cu = chi_so_cu
        self.chi_so_moi = chi_so_moi
        self.tong_tien = self.tinh_tien()

    def tinh_tien(self):
        tieu_thu = self.chi_so_moi - self.chi_so_cu
        if tieu_thu <= 50:
            tien = tieu_thu * 100
        elif tieu_thu <= 100:
            tien = 50 * 100 + (tieu_thu - 50) * 150
        else:
            tien = 50 * 100 + 50 * 150 + (tieu_thu - 100) * 200
        
        if tieu_thu <= 50:
            phu_phi = tien * 0.02
        elif tieu_thu > 50 and tieu_thu <= 100:
            phu_phi = tien * 0.03
        else:
            phu_phi = tien * 0.05

        return round(tien + phu_phi)
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.tong_tien}"
     

so_khach_hang = int(input())

khach_hang_list = []

for i in range(1, so_khach_hang + 1):
    ten = input().strip()
    chi_so_cu = int(input())
    chi_so_moi = int(input())
    khach_hang_list.append(KhachHang(i, ten, chi_so_cu, chi_so_moi))

khach_hang_list.sort(key = lambda x : x.tong_tien, reverse= True)


for i in khach_hang_list:
    print(i)




