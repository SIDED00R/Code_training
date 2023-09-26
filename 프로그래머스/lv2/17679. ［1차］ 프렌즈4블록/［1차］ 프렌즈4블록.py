def solution(m, n, board):
    board = list(map(list, zip(*board[::-1])))
    
    while True:
    
        find = []


        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] != 0:
                    if board[i][j] == board[i+1][j]:
                        if board[i][j] == board[i][j+1]:
                            if board[i][j] == board[i+1][j+1]:
                                find.append([i, j])
        if len(find) == 0:
            break

        for i, j in find:
            board[i][j] = board[i+1][j] = board[i][j+1] = board[i+1][j+1] = 0

        for i in range(n):
            newlist = []
            for j in range(m):
                if board[i][j] != 0:
                    newlist.append(board[i][j])
            while len(newlist) != m:
                newlist.append(0)
            board[i] = newlist
            
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                answer += 1
    
    return answer
                
                        
            