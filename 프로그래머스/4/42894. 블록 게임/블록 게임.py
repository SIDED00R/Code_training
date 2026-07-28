def check(board, i, j, n):
    now_num = board[i][j]

    #1
    find = False
    count = 0
    if i + 1 < n and 0 <= j - 2:
        for di in range(2):
            for dj in range(3):
                ni = i + di
                nj = j - dj
                if board[ni][nj] == now_num:
                    count += 1
                elif board[ni][nj] == -1:
                    continue
                else:
                    count = -6
        if count == 4:
            find = True
        if find:
            for ni in range(i, n):
                for dj in range(3):
                    nj = j - dj
                    if ni == 0:
                        if board[ni][nj] in [0, now_num]:
                            board[ni][nj] = -1
                    else:
                        if board[ni][nj] in [0, now_num] and board[ni - 1][nj] == -1:
                            board[ni][nj] = -1
            return True
    #2
    count = 0
    if i + 1 < n and j + 2 < n:
        for di in range(2):
            for dj in range(3):
                ni = i + di
                nj = j + dj
                if board[ni][nj] == now_num:
                    count += 1
                elif board[ni][nj] == -1:
                    continue
                else:
                    count = -6
        if count == 4:
            find = True
        if find:
            for ni in range(i, n):
                for dj in range(3):
                    nj = j + dj
                    if ni == 0:
                        if board[ni][nj] in [0, now_num]:
                            board[ni][nj] = -1
                    else:
                        if board[ni][nj] in [0, now_num] and board[ni - 1][nj] == -1:
                            board[ni][nj] = -1
            return True
    #3
    count = 0
    if i + 2 < n and 0 <= j - 1:
        for di in range(3):
            for dj in range(2):
                ni = i + di
                nj = j - dj
                if board[ni][nj] == now_num:
                    count += 1
                elif board[ni][nj] == -1:
                    continue
                else:
                    count = -6
        if count == 4:
            find = True
        if find:
            for ni in range(i, n):
                for dj in range(2):
                    nj = j - dj
                    if ni == 0:
                        if board[ni][nj] in [0, now_num]:
                            board[ni][nj] = -1
                    else:
                        if board[ni][nj] in [0, now_num] and board[ni - 1][nj] == -1:
                            board[ni][nj] = -1
            return True
    #4
    count = 0
    if i + 2 < n and j + 1 < n:
        for di in range(3):
            for dj in range(2):
                ni = i + di
                nj = j + dj
                if board[ni][nj] == now_num:
                    count += 1
                elif board[ni][nj] == -1:
                    continue
                else:
                    count = -6
        if count == 4:
            find = True
        if find:
            for ni in range(i, n):
                for dj in range(2):
                    nj = j + dj
                    if ni == 0:
                        if board[ni][nj] in [0, now_num]:
                            board[ni][nj] = -1
                    else:
                        if board[ni][nj] in [0, now_num] and board[ni - 1][nj] == -1:
                            board[ni][nj] = -1
            return True
    #5
    count = 0
    if i + 1 < n and j + 1 < n and 0 <= j - 1:
        for di in range(2):
            for dj in [-1, 0, 1]:
                ni = i + di
                nj = j + dj
                if board[ni][nj] == now_num:
                    count += 1
                elif board[ni][nj] == -1:
                    continue
                else:
                    count = -6
        if count == 4:
            find = True
        if find:
            for ni in range(i, n):
                for dj in [-1, 0, 1]:
                    nj = j + dj
                    if ni == 0:
                        if board[ni][nj] in [0, now_num]:
                            board[ni][nj] = -1
                    else:
                        if board[ni][nj] in [0, now_num] and board[ni - 1][nj] == -1:
                            board[ni][nj] = -1
            return True
        
    #6
    count = 0
    if i + 1 < n and 0 <= i - 1 and j + 1 < n:
        for di in [-1, 0, 1]:
            for dj in range(2):
                ni = i + di
                nj = j + dj
                if board[ni][nj] == now_num:
                    count += 1
                elif board[ni][nj] == -1:
                    continue
                else:
                    count = -6
        if count == 4:
            find = True
        if find:
            for ni in range(i - 1, n):
                for dj in range(2):
                    nj = j + dj
                    if ni == 0:
                        if board[ni][nj] in [0, now_num]:
                            board[ni][nj] = -1
                    else:
                        if board[ni][nj] in [0, now_num] and board[ni - 1][nj] == -1:
                            board[ni][nj] = -1
            return True

def solution(board):
    for l in board:
        print(l)
    n = len(board)
    for i in range(n):
        for j in range(n):
            if i == 0 and board[i][j] == 0:
                board[i][j] = -1
            elif board[i][j] == 0 and board[i - 1][j] == -1:
                board[i][j] = -1
    
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] not in [0, -1]:
                if check(board, i, j, n):
                    answer += 1
    for l in board:
        print(l)                
    return answer