n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, list(input()))))

min_length = min(n, m)
for length in range(min_length, 0, -1):
    for i in range(n - length + 1):
        for j in range(m - length + 1):
            if matrix[i][j] == matrix[i][j + length - 1] == matrix[i + length - 1][j] == matrix[i + length - 1][j + length - 1]:
                print(length ** 2)
                exit()
            
            