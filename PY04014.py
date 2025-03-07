import sys
from decimal import Decimal, ROUND_HALF_UP

class HocSinh:
    def __init__(self, ma, ten, diem):
        self.ma = f"HS{ma:02d}"
        self.ten = ten
        self.diem = [Decimal(d) for d in diem]
        self.diem_tb = self.tinh_diem_tb()
        self.xep_loai = self.xep_loai_hs()
    
    def tinh_diem_tb(self):
        tong_diem = self.diem[0] * 2 + self.diem[1] * 2 + sum(self.diem[2:])
        diem_tb = (tong_diem / Decimal(12)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        return diem_tb
    
    def xep_loai_hs(self):
        if self.diem_tb >= Decimal(9):
            return "XUAT SAC"
        elif self.diem_tb >= Decimal(8):
            return "GIOI"
        elif self.diem_tb >= Decimal(7):
            return "KHA"
        elif self.diem_tb >= Decimal(5):
            return "TB"
        else:
            return "YEU"
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.diem_tb} {self.xep_loai}"

def giai_quyet():
    so_hoc_sinh = int(input().strip())
    danh_sach_hs = []
    
    for i in range(1, so_hoc_sinh + 1):
        ten = input().strip()
        diem = input().strip().split()
        danh_sach_hs.append(HocSinh(i, ten, diem))
    
    danh_sach_hs.sort(key=lambda hs: (-hs.diem_tb, hs.ma))
    
    for hs in danh_sach_hs:
        print(hs)

if __name__ == "__main__":
    giai_quyet()
