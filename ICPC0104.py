import re

def check(s):
    numbers = list(map(int,re.findall(r'\d+', s)))
    return max(numbers) if numbers else None

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    print(check(s))


