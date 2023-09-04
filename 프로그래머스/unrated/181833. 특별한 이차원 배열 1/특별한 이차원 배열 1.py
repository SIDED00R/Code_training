def solution(n):
    solution = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                solution[i][j] = 1
    return solution