from math import gcd
from sys import stdin

class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.rut_gon()

    def rut_gon(self):
        ucln = gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

    def cong(self, phan_so_khac):
        tu_moi = self.tu_so * phan_so_khac.mau_so + phan_so_khac.tu_so * self.mau_so
        mau_moi = self.mau_so * phan_so_khac.mau_so
        return PhanSo(tu_moi, mau_moi)

    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"

if __name__ == "__main__":
    tu1, mau1, tu2, mau2 = map(int, stdin.readline().split())
    p = PhanSo(tu1, mau1)
    q = PhanSo(tu2, mau2)
    tong_phan_so = p.cong(q)
    print(tong_phan_so)
