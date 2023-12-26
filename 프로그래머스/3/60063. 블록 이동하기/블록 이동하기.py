def solution(board):
    N = len(board)
    block = [1] * (N + 2)
    board = [block] + [[1] + line + [1] for line in board] + [block]
    for i in range(N + 2):
        for j in range(N + 2):
            if board[i][j] == 0:
                board[i][j] = [10000, 10000]
    state = {"h" : 0, "v" : 1} # h: horizontal, v: vertical 
    
    stack = [[1, 2, "h"]] # 오른쪽 아래의 좌표, 드론의 상태
    board[1][2][0] = 0
    now_num = 0
    while board[N][N] == [10000, 10000]:
        now_num += 1
        new_stack = []
        while stack:
            now_i, now_j, s = stack.pop()
            if s == "h":
                before_i = now_i
                before_j = now_j - 1
            else:
                before_i = now_i - 1
                before_j = now_j
            # 상하좌우 이동
            if board[now_i - 1][now_j] != 1 and board[before_i - 1][before_j] != 1 and board[now_i - 1][now_j][state[s]] > now_num:
                board[now_i - 1][now_j][state[s]] = now_num
                new_stack.append([now_i - 1, now_j, s])
            if board[now_i + 1][now_j] != 1 and board[before_i + 1][before_j] != 1 and board[now_i + 1][now_j][state[s]] > now_num:
                board[now_i + 1][now_j][state[s]] = now_num
                new_stack.append([now_i + 1, now_j, s])
            if board[now_i][now_j - 1] != 1 and board[before_i][before_j - 1] != 1 and board[now_i][now_j - 1][state[s]] > now_num:
                board[now_i][now_j - 1][state[s]] = now_num
                new_stack.append([now_i, now_j - 1, s])
            if board[now_i][now_j + 1] != 1 and board[before_i][before_j + 1] != 1 and board[now_i][now_j + 1][state[s]] > now_num:
                board[now_i][now_j + 1][state[s]] = now_num
                new_stack.append([now_i, now_j + 1, s])
            # 회전 이동
            if s == "h":
                if board[now_i + 1][now_j - 1] != 1 and board[now_i + 1][now_j] != 1 and board[now_i + 1][now_j][1] > now_num:
                    board[now_i + 1][now_j][1] = now_num
                    new_stack.append([now_i + 1, now_j, "v"])
                if board[now_i + 1][now_j - 1] != 1 and board[now_i + 1][now_j] != 1 and board[now_i + 1][now_j - 1][1] > now_num:
                    board[now_i + 1][now_j - 1][1] = now_num
                    new_stack.append([now_i + 1, now_j - 1, "v"])
                if board[now_i - 1][now_j - 1] != 1 and board[now_i - 1][now_j] != 1 and board[now_i][now_j][1] > now_num:
                    board[now_i][now_j][1] = now_num
                    new_stack.append([now_i, now_j, "v"])
                if board[now_i - 1][now_j - 1] != 1 and board[now_i - 1][now_j] != 1 and board[now_i][now_j - 1][1] > now_num:
                    board[now_i][now_j - 1][1] = now_num
                    new_stack.append([now_i, now_j - 1, "v"])
            else:
                if board[now_i][now_j + 1] != 1 and board[now_i - 1][now_j + 1] != 1 and board[now_i][now_j + 1][0] > now_num:
                    board[now_i][now_j + 1][0] = now_num
                    new_stack.append([now_i, now_j + 1, "h"])
                if board[now_i][now_j + 1] != 1 and board[now_i - 1][now_j + 1] != 1 and board[now_i - 1][now_j + 1][0] > now_num:
                    board[now_i - 1][now_j + 1][0] = now_num
                    new_stack.append([now_i - 1, now_j + 1, "h"])
                if board[now_i][now_j - 1] != 1 and board[now_i - 1][now_j - 1] != 1 and board[now_i][now_j][0] > now_num:
                    board[now_i][now_j][0] = now_num
                    new_stack.append([now_i, now_j, "h"])
                if board[now_i][now_j - 1] != 1 and board[now_i - 1][now_j - 1] != 1 and board[now_i - 1][now_j][0] > now_num:
                    board[now_i - 1][now_j][0] = now_num
                    new_stack.append([now_i - 1, now_j, "h"])
        stack = new_stack[:]

    return min(board[N][N])