class ThiSinh:
    def __init__(self, ma, ho_ten, ly_thuyet, thuc_hanh):
        self.ma = ma
        self.ho_ten = ho_ten
        self.ly_thuyet = self.chuan_hoa_diem(ly_thuyet)
        self.thuc_hanh = self.chuan_hoa_diem(thuc_hanh)
        self.trung_binh = (self.ly_thuyet + self.thuc_hanh) / 2
        self.xep_loai = self.lay_xep_loai()

    def chuan_hoa_diem(self, diem):
        diem = float(diem)
        if diem > 10:
            diem /= 10
        return diem

    def lay_xep_loai(self):
        if self.trung_binh < 5:
            return "TRUOT"
        elif self.trung_binh < 8:
            return "CAN NHAC"
        elif self.trung_binh <= 9.5:
            return "DAT"
        else:
            return "XUAT SAC"

    def __str__(self):
        return f"{self.ma} {self.ho_ten} {self.trung_binh:.2f} {self.xep_loai}"


def main():
    so_thi_sinh = int(input())
    danh_sach_thi_sinh = []

    for i in range(1, so_thi_sinh + 1):
        ho_ten = input().strip()
        ly_thuyet = input().strip()
        thuc_hanh = input().strip()
        ma = f"TS{str(i).zfill(2)}"
        danh_sach_thi_sinh.append(ThiSinh(ma, ho_ten, ly_thuyet, thuc_hanh))

    danh_sach_thi_sinh.sort(key=lambda ts: ts.trung_binh, reverse=True)

    for thi_sinh in danh_sach_thi_sinh:
        print(thi_sinh)


if __name__ == "__main__":
    main()
