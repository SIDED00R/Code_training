while True:
    w, h = map(int, input().split())
    answer = 0
    if w == 0 and h == 0:
        break
    matrix = []
    visite_matrix = [[0 for _ in range(w)] for _ in range(h)]

    for _ in range(h):
        matrix.append(list(input()))

    for i in range(h):
        for j in range(w):
            if matrix[i][j].isnumeric():
                visite_matrix[i][j] = max(int(matrix[i][j]), visite_matrix[i][j])
                answer = max(answer, visite_matrix[i][j])
                if 0 <= i + 1 < h and matrix[i + 1][j].isnumeric():
                    visite_matrix[i + 1][j] = max(visite_matrix[i + 1][j], visite_matrix[i][j] * 10 + int(matrix[i + 1][j]))
                    answer = max(answer, visite_matrix[i + 1][j])
                if 0 <= j + 1 < w and matrix[i][j + 1].isnumeric():
                    visite_matrix[i][j + 1] = max(visite_matrix[i][j + 1], visite_matrix[i][j] * 10 + int(matrix[i][j + 1]))
                    answer = max(answer, visite_matrix[i][j + 1])

    print(answer)

