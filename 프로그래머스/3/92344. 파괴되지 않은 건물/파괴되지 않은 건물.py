def solution(board, skill):
    N = len(board)
    M = len(board[0])
    new_board = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for case in skill:
        t, r1, c1, r2, c2, degree = case
        degree = degree * (2 * t - 3)
        new_board[r1][c1] += degree
        new_board[r1][c2 + 1] -= degree
        new_board[r2 + 1][c1] -= degree
        new_board[r2 + 1][c2 + 1] += degree

    answer = 0
    for i in range(N):
        for j in range(M):
            new_board[i][j + 1] += new_board[i][j]
    for i in range(N):
        for j in range(M):
            new_board[i + 1][j] += new_board[i][j]
            if new_board[i][j] + board[i][j] > 0:
                answer += 1

    return answer