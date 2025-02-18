n = int(input())
num = (n - 1) // 8 + 1
alp = (n - 1) % 8 + 1
print(f"{chr(96 + alp)}{num}")