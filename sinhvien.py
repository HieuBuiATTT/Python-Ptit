text = "Python is fun Python is easy to learn Python is  powerful".split()

t = {}

for i in text:
    if i not in t.keys():
        t[i] = 1
    else:
        t[i] += 1
for i in t.keys():
    print(i, t[i])