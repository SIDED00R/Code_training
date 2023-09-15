def solution(park, routes):
    find = False
    row, col = len(park), len(park[0])
    for i in range(row):
        for j in range(col):
            if park[i][j] == "S":
                x, y = j, i
                find = True
                break
        if find:
            break
    
    now = [y, x]
    
    for route in routes:
        move = [now[0], now[1]]
        derection, num = route.split()
        
        for _ in range(int(num)):   
            if derection == "N":
                if move[0] - 1 < 0 or park[move[0] - 1][move[1]] == "X":
                    move = now
                    break
                else:
                    move[0] -= 1              
            elif derection == "S":
                if move[0] + 1 >= row or park[move[0] + 1][move[1]] == "X":
                    move = now
                    break
                else:
                    move[0] += 1    
            elif derection == "W":
                if move[1] - 1 < 0 or park[move[0]][move[1] - 1] == "X":
                    move = now
                    break
                else:
                    move[1] -= 1
            elif derection == "E":
                if move[1] + 1 >= col or park[move[0]][move[1] + 1] == "X":
                    move = now
                    break
                else:
                    move[1] += 1
        now = move
                    
    return now