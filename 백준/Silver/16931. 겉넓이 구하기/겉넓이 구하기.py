n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
    
answer = n * m * 2
add = 0
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for i in range(n):
    for j in range(m):
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if 0 <= ni < n and 0 <= nj < m:
                add += abs(matrix[i][j] - matrix[ni][nj])
            else:
                add += matrix[i][j] * 2
print(answer + add // 2)