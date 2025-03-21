# Đọc số lượng giám khảo
N = int(input().strip())

# Đọc danh sách điểm số
diem = list(map(float, input().split()))

# Tìm giá trị nhỏ nhất và lớn nhất
diem_min = min(diem)
diem_max = max(diem)

# Lọc bỏ tất cả điểm trùng với giá trị nhỏ nhất và lớn nhất
diem_con_lai = [x for x in diem if x != diem_min and x != diem_max]

# Tính điểm trung bình các giá trị còn lại
diem_trung_binh = sum(diem_con_lai) / len(diem_con_lai)

# In ra kết quả với 2 chữ số sau dấu phẩy
print(f"{diem_trung_binh:.2f}")
