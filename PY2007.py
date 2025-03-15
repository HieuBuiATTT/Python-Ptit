
import sys
# Đọc tất cả dòng, tách thành các số nguyên
numbers = list(map(int, sys.stdin.read().split()))

# Tạo set chứa các phần dư khi chia cho 42
remainders = {num % 42 for num in numbers}

# In ra số lượng phần dư khác nhau
print(len(remainders))


