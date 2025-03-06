def find_lucky_number(matrix, n, m):
    min_val = min(min(row) for row in matrix)
    max_val = max(max(row) for row in matrix)
    lucky_number = max_val - min_val
    
    positions = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == lucky_number:
                positions.append((i, j))
    
    if positions:
        print(lucky_number)
        for pos in positions:
            print(f"Vi tri [{pos[0]}][{pos[1]}]")
    else:
        print("NOT FOUND")

# Đọc dữ liệu đầu vào
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Tìm số may mắn và in kết quả
find_lucky_number(matrix, n, m)

