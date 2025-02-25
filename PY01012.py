s1 = input().strip()
s2 = input().strip()

p = int(input())

ketqua = s1[:p - 1] + s2 + s1[p-1:]

print(ketqua)