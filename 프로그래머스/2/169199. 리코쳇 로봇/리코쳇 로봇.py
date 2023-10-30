def move(board, start, count):
    i, j = start
    
    if isinstance(board[i - 1][j], int):
        ui = i
        while board[ui - 1][j] != "D":
            ui -= 1
        if board[ui][j] == 0 or board[ui][j] > count + 1:
            board[ui][j] = count + 1
            move(board, [ui, j], count + 1)

    if isinstance(board[i + 1][j], int):
        di = i
        while board[di + 1][j] != "D":
            di += 1
        if board[di][j] == 0 or board[di][j] > count + 1:
            board[di][j] = count + 1
            move(board, [di, j], count + 1)
    
    if isinstance(board[i][j + 1], int):
        rj = j
        while board[i][rj + 1] != "D":
            rj += 1
        if board[i][rj] == 0 or board[i][rj] > count + 1:
            board[i][rj] = count + 1
            move(board, [i, rj], count + 1)
    
    if isinstance(board[i][j - 1], int):
        lj = j
        while board[i][lj - 1] != "D":
            lj -= 1
        if board[i][lj] == 0 or board[i][lj] > count + 1:
            board[i][lj] = count + 1
            move(board, [i, lj], count + 1)
    
    return board

    

def solution(board):
    bound = ["D"] * (len(board[0]) + 2)
    board = [bound] + [["D"] + list(line) + ["D"] for line in board] + [bound]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "G":
                goal = [i, j]
            elif board[i][j] == "R":
                start = [i, j]
            if board[i][j] != "D":
                board[i][j] = 0
                
    move(board, start, 0)  
    
    return -1 if board[goal[0]][goal[1]] == 0 else board[goal[0]][goal[1]]