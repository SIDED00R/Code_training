n, m = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(input())
    matrix.append(line)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
count = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        c = 1
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if 0 <= ni < n and 0 <= nj < m:
                c += 1
        count[i][j] = c

answer = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (matrix[i][j] == 'W' and count[i][j] % 2 == 0) or (matrix[i][j] == 'B' and count[i][j] % 2 == 1):
            answer[i][j] = 3
        else:
            answer[i][j] = 2

print(1)
for l in answer:
    print("".join(map(str, l)))