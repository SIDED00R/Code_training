n = int(input())
matrix = []

for _ in range(2 * n):
    num = int(input())
    matrix.append(num)

matrix.sort()

first_sum = []
total = 0
for i in range(-1, -n - 1, -1):
    total += matrix[i]
    first_sum.append(total)

second_sum = [0]
total = 0
for i in range(1, 2 * n - 1, 2):
    total += matrix[i]
    second_sum.append(total)

answer = 1e20
for i in range(n):
    second_line_size = matrix[-i - 2]
    col = second_line_size + matrix[-1]
    row = first_sum[i] + second_sum[-i - 1]
    answer = min(answer, col * row)

print(answer)
    