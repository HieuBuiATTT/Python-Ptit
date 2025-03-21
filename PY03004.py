import re
from collections import Counter

# Đọc số dòng
N = int(input().strip())

# Đọc đoạn văn bản
text = "".join(input().strip().lower() for _ in range(N))

# Loại bỏ dấu câu, chỉ giữ lại từ và số
words = re.findall(r"\w+", text)

# Đếm tần suất các từ
word_count = Counter(words)

# Sắp xếp theo tần suất giảm dần, từ điển tăng dần nếu tần suất bằng nhau
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

# In kết quả
for word, count in sorted_words:
    print(word, count)
