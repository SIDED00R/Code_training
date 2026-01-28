n = int(input())
m = int(((8 * n + 1) ** 0.5 - 1) // 2)
answer = pow(2, m, 9901) * (n - m * (m - 1) // 2 - 1) + 1
print(answer % 9901)