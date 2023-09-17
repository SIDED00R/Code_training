def solution(board):
    m = board[0][0]
    for i in range(len(board) - 1):
        for j in range(len(board[i]) - 1):
            if board[i][j] == board[i + 1][j] == board[i][j + 1] and board[i + 1][j + 1] == 1:
                board[i + 1][j + 1] = board[i][j] + 1
                if m < board[i][j] + 1:
                    m = board[i][j] + 1
            elif board[i + 1][j + 1] == 1:
                low = min(board[i][j], board[i + 1][j], board[i][j + 1])
                board[i + 1][j + 1] = low + 1

    return m * m