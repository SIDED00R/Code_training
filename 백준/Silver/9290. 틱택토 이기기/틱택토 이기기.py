n = int(input())
for idx in range(n):
    matrix = []
    for _ in range(3):
        matrix.append(list(input()))
    sim = input()
    find = False
    for i in range(3):
        if find:
            break
        for j in range(3):
            if matrix[i][j] != '-':
                continue
            if (matrix[i][(j + 1) % 3] == sim) and (matrix[i][(j + 2) % 3] == sim):
                matrix[i][j] = sim
                find = True
                break
            if (matrix[(i + 1) % 3][j] == sim) and (matrix[(i + 2) % 3][j] == sim):
                matrix[i][j] = sim
                find = True
                break
            if (i * 3 + j) in [0, 4, 8]:
                if (matrix[(i + 1) % 3][(j + 1) % 3] == sim) and (matrix[(i + 2) % 3][(j + 2) % 3] == sim):
                    matrix[i][j] = sim
                    find = True
                    break
            if (i * 3 + j) in [2, 4, 6]:
                if (matrix[(i + 1) % 3][(j - 1) % 3] == sim) and (matrix[(i + 2) % 3][(j - 2) % 3] == sim):
                    matrix[i][j] = sim
                    find = True
                    break
    print(f'Case {idx + 1}:')
    for l in matrix:  
        print("".join(l))
                