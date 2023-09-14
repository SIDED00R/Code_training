def solution(wallpaper):
    row, col = len(wallpaper), len(wallpaper[0])
    lux, luy, rdx, rdy = row, col, 0, 0
    for i in range(row):
        for j in range(col):
            if wallpaper[i][j] == "#":
                lux, luy, rdx, rdy = min(lux, i), min(luy, j), max(rdx, i), max(rdy, j)
                
            
    return [lux, luy, rdx + 1, rdy + 1]