N, M = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)
    
for i in range(N):
    for j in range(M - 1):
        if i != 0:
            if j == 0:
                matrix[i][j] += matrix[i - 1][j]
            matrix[i][j + 1] = matrix[i][j] + matrix[i - 1][j + 1] - matrix[i - 1][j] + matrix[i][j + 1]
        else:
            matrix[i][j + 1] = matrix[i][j] + matrix[i][j + 1]
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    x -= 1
    y -= 1
    total = 0
    total += matrix[x][y]
    if i != 1 and j != 1:
        total += (matrix[i - 2][j - 2] - matrix[i - 2][y] - matrix[x][j - 2])
    elif i != 1:
        total -= matrix[i - 2][y]
    elif j != 1:
        total -= matrix[x][j - 2]
        
    print(total)