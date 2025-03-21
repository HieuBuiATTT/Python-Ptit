def liet_ke_hoan_vi(chuoi, l, r):
    if l == r:
        print("".join(chuoi))
    else:
        for i in range(l, r + 1):
            # Hoán đổi vị trí l và i
            chuoi[l], chuoi[i] = chuoi[i], chuoi[l]
            # Đệ quy tạo hoán vị cho phần còn lại
            liet_ke_hoan_vi(chuoi, l + 1, r)
            # Hoán đổi lại để quay lui
            chuoi[l], chuoi[i] = chuoi[i], chuoi[l]

# Đọc chuỗi đầu vào
S = input().strip()

# Chuyển chuỗi thành danh sách ký tự
chuoi = list(S)

# Đảm bảo chuỗi luôn sắp xếp đúng thứ tự từ điển
chuoi.sort()

# Gọi hàm tạo hoán vị từ vị trí đầu tiên
liet_ke_hoan_vi(chuoi, 0, len(S) - 1)
