def find_empty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return -1, -1

def able_num(sudoku, now, num):
    now_i, now_j = now
    area_i = now_i // 3
    area_j = now_j // 3
    for i in range(3):
        for j in range(3):
            if sudoku[area_i * 3 + i][area_j * 3 + j] == num:
                return False
    for i in range(9):
        if sudoku[i][now_j] == num:
            return False
        if sudoku[now_i][i] == num:
            return False
    return True

def check(sudoku):
    i, j = find_empty(sudoku)
    if i == -1:
        return True
    for num in range(1, 10):
        if able_num(sudoku, [i, j], num):
            sudoku[i][j] = num
            if check(sudoku):
                return True
            sudoku[i][j] = 0
    return False
        
sudoku = []
for _ in range(9):
    line = list(map(int, list(input())))
    sudoku.append(line)
    
check(sudoku)
for line in sudoku:
    for num in line:
        print(num, end = "")
    print()
