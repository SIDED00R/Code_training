import sys
sys.setrecursionlimit(10 ** 6)

def sudoku(idx):
    if idx == len(blanks):
        for l in matrix:
            print(" ".join(map(str, l)))
        exit()

    i, j = blanks[idx]
    b = (i // 3) * 3 + (j // 3)

    for num in range(1, 10):
        if row[i][num] or col[j][num] or box[b][num]:
            continue

        matrix[i][j] = num
        row[i][num] = col[j][num] = box[b][num] = True

        sudoku(idx + 1)
        matrix[i][j] = 0
        row[i][num] = col[j][num] = box[b][num] = False
matrix = [list(map(int, input().split())) for _ in range(9)]
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
box = [[False] * 10 for _ in range(9)]

blanks = []

for i in range(9):
    for j in range(9):
        num = matrix[i][j]
        if num == 0:
            blanks.append((i, j))
        else:
            row[i][num] = True
            col[j][num] = True
            b = (i // 3) * 3 + (j // 3)
            box[b][num] = True

sudoku(0)