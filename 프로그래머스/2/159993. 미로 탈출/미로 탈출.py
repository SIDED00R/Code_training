import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

def find(maps, now, count):
    i, j = now
    
    if maps[i - 1][j] != "X":
        if  maps[i - 1][j] == 0 or maps[i - 1][j] > count + 1:
            maps[i - 1][j] = count + 1
            find(maps, [i - 1, j], count + 1)

    if maps[i + 1][j] != "X":
        if  maps[i + 1][j] == 0 or maps[i + 1][j] > count + 1:
            maps[i + 1][j] = count + 1
            find(maps, [i + 1, j], count + 1)

    if maps[i][j + 1] != "X":
        if  maps[i][j + 1] == 0 or maps[i][j + 1] > count + 1:
            maps[i][j + 1] = count + 1
            find(maps, [i, j + 1], count + 1)
        
    if maps[i][j - 1] != "X":
        if  maps[i][j - 1] == 0 or maps[i][j - 1] > count + 1:
            maps[i][j - 1] = count + 1
            find(maps, [i, j - 1], count + 1)
        
    return maps
    
    

def solution(maps):
    col = len(maps[0])
    bound = ["X"] * (col + 2)
    maps = [bound] + [["X"] + list(line) + ["X"] for line in maps] + [bound]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = [i, j]
            elif maps[i][j] == "L":
                lever = [i, j]
            elif maps[i][j] == "E":
                end = [i, j]
            if maps[i][j] != "X":
                maps[i][j] = 0
                
    find(maps, lever, 0)
    end_count = maps[end[0]][end[1]]
    lever_count = maps[start[0]][start[1]]
    
    if maps[end[0]][end[1]] != 0 and maps[start[0]][start[1]] != 0:
        return lever_count + end_count
    else:
        return -1

