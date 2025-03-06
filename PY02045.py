def split_and_sum(number: str):
    while len(number) > 1:
        n = len(number)
        mid = n // 2
        left_part = int(number[:mid])
        right_part = int(number[mid:])
        number = str(left_part + right_part)
        print(number)

# Đọc input từ người dùng
number = input().strip()
split_and_sum(number)
