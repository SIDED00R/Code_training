n = int(input())
y = 2024
m = 1 + 7 * n
y += (m - 1) // 12
m = ((m - 1) % 12) + 1
print(y, m)
