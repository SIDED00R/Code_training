import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

def island(maps, i, j):
    answer = int(maps[i][j])
    maps[i][j] = "X"
    if maps[i - 1][j] != "X":
        answer += island(maps, i - 1, j)
    
    if maps[i + 1][j] != "X":
        answer += island(maps, i + 1, j)
    
    if maps[i][j + 1] != "X":
        answer += island(maps, i, j + 1)
        
    if maps[i][j - 1] != "X":
        answer += island(maps, i, j - 1)
    
    return answer
        
        

def solution(maps):
    bound = ["X"] * (len(maps[0]) + 2)
    maps = [bound] + [["X"] + list(line) + ["X"] for line in maps] + [bound]
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X":
                answer.append(island(maps, i, j))

    return [-1] if answer == [] else sorted(answer)