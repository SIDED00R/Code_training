import sys
n = int(input())
line = list(sys.stdin.readline().rstrip('\n'))
matrix = [line[n // 5 * num:n // 5 * (num + 1)] for num in range(5)]

def check(i, j):
    if j + 2 >= n // 5:
        return "1"
    if matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 3][j] == matrix[i + 4][j] == matrix[i][j + 1] == matrix[i + 2][j + 1] == matrix[i + 4][j + 1] == matrix[i][j + 2] == matrix[i + 1][j + 2] == matrix[i + 2][j + 2] == matrix[i + 3][j + 2] == matrix[i + 4][j + 2] == "#":
        return "8"
    elif matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 4][j] == matrix[i][j + 1] == matrix[i + 2][j + 1] == matrix[i + 4][j + 1] == matrix[i][j + 2] == matrix[i + 1][j + 2] == matrix[i + 2][j + 2] == matrix[i + 3][j + 2] == matrix[i + 4][j + 2] == "#":
        return "9"
    elif matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 3][j] == matrix[i + 4][j] == matrix[i][j + 1] == matrix[i + 2][j + 1] == matrix[i + 4][j + 1] == matrix[i][j + 2] == matrix[i + 2][j + 2] == matrix[i + 3][j + 2] == matrix[i + 4][j + 2] == "#":
        return "6"
    elif matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 3][j] == matrix[i + 4][j] == matrix[i][j + 1] == matrix[i + 4][j + 1] == matrix[i][j + 2] == matrix[i + 1][j + 2] == matrix[i + 2][j + 2] == matrix[i + 3][j + 2] == matrix[i + 4][j + 2] == "#":
        return "0"
    elif matrix[i + 2][j] == matrix[i + 3][j] == matrix[i + 4][j] == matrix[i][j + 1] == matrix[i + 2][j + 1] == matrix[i + 4][j + 1] == matrix[i][j + 2] == matrix[i + 1][j + 2] == matrix[i + 2][j + 2] == matrix[i + 4][j + 2] == "#":
        return "2"
    elif matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 4][j] == matrix[i][j + 1] == matrix[i + 2][j + 1] == matrix[i + 4][j + 1] == matrix[i][j + 2] == matrix[i + 2][j + 2] == matrix[i + 3][j + 2] == matrix[i + 4][j + 2] == "#":
        return "5"
    elif matrix[i + 2][j] == matrix[i + 4][j] == matrix[i][j + 1] == matrix[i + 2][j + 1] == matrix[i + 4][j + 1] == matrix[i][j + 2] == matrix[i + 1][j + 2] == matrix[i + 2][j + 2] == matrix[i + 3][j + 2] == matrix[i + 4][j + 2] == "#":
        return "3"
    elif matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 2][j + 1] == matrix[i][j + 2] == matrix[i + 1][j + 2] == matrix[i + 2][j + 2] == matrix[i + 3][j + 2] == matrix[i + 4][j + 2] == "#":
        return "4"
    elif matrix[i][j + 1] == matrix[i][j + 2] == matrix[i + 1][j + 2] == matrix[i + 2][j + 2] == matrix[i + 3][j + 2] == matrix[i + 4][j + 2] == "#":
        return "7"
    else:
        return "1"

answer = ""
idx = 0
while idx < n // 5:
    if matrix[0][idx] == "#":
        now = check(0, idx)
        answer += now
        if now == "1":
            idx += 1
        else:
            idx += 3
    idx += 1
        
print(answer)