def mini_count(i, j):
    return (i + 1) * i // 2 * (j + 1) * j // 2

def count(i, j, total, n, m):
    answer = total
    answer -= mini_count(i - 1, 2 * m)
    answer -= mini_count(j - 1, 2 * n)
    answer -= mini_count(2 * n - i, 2 * m)
    answer -= mini_count(2 * m - j, 2 * n)
    answer += mini_count(i - 1, j - 1)
    answer += mini_count(i - 1, 2 * m - j)
    answer += mini_count(2 * n - i, j - 1)
    answer += mini_count(2 * n - i, 2 * m - j)
    return answer

n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]

total = mini_count(2 * n, 2 * m)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        matrix[i - 1][j - 1] = count(i, j, total, n, m)
dic = {}
for i in range(26):
    dic[chr(65 + i)] = 0

alp_matrix = []
for _ in range(n):
    alp_matrix.append(list(input()))

for i in range(n):
    for j in range(m):
        dic[alp_matrix[i][j]] += (matrix[i][j] + matrix[-i - 1][j] + matrix[i][-j - 1] + matrix[-i - 1][-j - 1])

for k, v in dic.items():
    print(v)