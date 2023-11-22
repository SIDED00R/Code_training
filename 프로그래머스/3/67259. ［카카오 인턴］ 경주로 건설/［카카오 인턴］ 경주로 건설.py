import sys
sys.setrecursionlimit(10000)

def move(now, board, before, now_num):
    i, j = now
    #아래
    if board[i + 1][j] != 1:  
        if before == "left" or before == "right":
            if board[i + 1][j][0] == 0 or board[i + 1][j][0] > now_num + 600:
                board[i + 1][j][0] = now_num + 600
                move([i + 1, j], board, "down", board[i + 1][j][0])
        else:
            if board[i + 1][j][0] == 0 or board[i + 1][j][0] > now_num + 100:
                board[i + 1][j][0] = now_num + 100
                move([i + 1, j], board, "down", board[i + 1][j][0])
                
    #위
    if board[i - 1][j] != 1:  
        if before == "left" or before == "right":
            if board[i - 1][j][1] == 0 or board[i - 1][j][1] > now_num + 600:
                board[i - 1][j][1] = now_num + 600
                move([i - 1, j], board, "up", board[i - 1][j][1])
        else:
            if board[i - 1][j][1] == 0 or board[i - 1][j][1] > now_num + 100:
                board[i - 1][j][1] = now_num + 100
                move([i - 1, j], board, "up", board[i - 1][j][1])
    #왼쪽
    if board[i][j - 1] != 1:  
        if before == "up" or before == "down":
            if board[i][j - 1][2] == 0 or board[i][j - 1][2] > now_num + 600:
                board[i][j - 1][2] = now_num + 600
                move([i, j - 1], board, "left", board[i][j - 1][2])
        else:
            if board[i][j - 1][2] == 0 or board[i][j - 1][2] > now_num + 100:
                board[i][j - 1][2] = now_num + 100
                move([i, j - 1], board, "left", board[i][j - 1][2])
    #오른쪽
    if board[i][j + 1] != 1:  
        if before == "up" or before == "down":
            if board[i][j + 1][3] == 0 or board[i][j + 1][3] > now_num + 600:
                board[i][j + 1][3] = now_num + 600
                move([i, j + 1], board, "right", board[i][j + 1][3])
        else:
            if board[i][j + 1][3] == 0 or board[i][j + 1][3] > now_num + 100:
                board[i][j + 1][3] = now_num + 100
                move([i, j + 1], board, "right", board[i][j + 1][3])


def solution(board):
    n = len(board)
    block = [1] * (n + 2)
    board = [block] + [[1] + line + [1] for line in board] + [block]
    for i in range(n + 2):
        for j in range(n + 2):
            if board[i][j] == 0:
                board[i][j] = [0, 0, 0, 0]
    start = [1, 1]
    move(start, board, "start", 0)
    
    answer = []
    for num in board[n][n]:
        if num != 0:
            answer.append(num)

    return min(answer)