def solution(m, n, puddles):
    land = [[1 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        x, y = puddle
        land[y-1][x-1] = 0
    
    p = False
    for i in range(n):
        if p:
            land[i][0] = 0
        if land[i][0] == 0:
            p = True
    
    p = False
    for j in range(m):
        if p:
            land[0][j] = 0
        if land[0][j] == 0:
            p = True
    
    for i in range(1, n):
        for j in range(1, m):
            if land[i][j] == 0:
                continue
            else:
                land[i][j] = land[i - 1][j] + land[i][j - 1] 
    return land[-1][-1] % 1000000007