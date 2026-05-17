t = int(input())
for _ in range(t):
    matrix = []
    for _ in range(9):
        matrix.append(list(map(int, list(input()))))
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 1:
                matrix[i][j] = 2
    for line in matrix:
        print("".join(map(str, line)))