s = input()
n = s[-3::]
print("yes" if n == '.py' or n == '.PY' or n == '.Py' or n == '.pY' else "no")