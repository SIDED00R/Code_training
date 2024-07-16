n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]

def able(i, j):
    if i > 0 and j > 0 and matrix[i - 1][j] == matrix[i][j - 1] == matrix[i - 1][j - 1] == 1:
        return False
    return True

answer = 0
def recursion(i, j):
    global answer
    if able(i, j):
        answer += 1
        if j == m - 1:
            if i == n - 1:
                return
            matrix[i][j] = 1
            recursion(i + 1, 0)
            matrix[i][j] = 0
            recursion(i + 1, 0)
        else:
            matrix[i][j] = 1
            recursion(i, j + 1)
            matrix[i][j] = 0
            recursion(i, j + 1)
    else:
        if j == m - 1:
            if i == n - 1:
                return
            matrix[i][j] = 0
            recursion(i + 1, 0)
        else:
            matrix[i][j] = 0
            recursion(i, j + 1)
         
recursion(0, 0)
print(answer + 1)
            