import math

class Phanso:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        self.rut_gon()
    def rut_gon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def __str__(self):
        return f"{self.tu}/{self.mau}"

tu, mau = [int(i) for i in input().split()]
phan_so =  Phanso(tu,mau)

print(phan_so)