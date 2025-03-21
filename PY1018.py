P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    # Đọc đầu vào
    line = input().strip()
    if line == "0":
        break
    
    # Tách số K và chuỗi S
    K, S = line.split()
    K = int(K)
    
    # Mã hóa từng ký tự
    encoded = "".join(P[(P.index(char) + K) % 28] for char in S)
    
    # Đảo ngược chuỗi kết quả
    result = encoded[::-1]
    
    # In kết quả
    print(result)
