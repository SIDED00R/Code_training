def solution(dirs):
    now = [0, 0]
    road = set()
    
    for move in dirs:
        if move == "U":
            if now[1] == 5:
                continue
            else:
                road.add((now[0], now[1], now[0], now[1] + 1))
                now =[now[0],now[1] + 1]
                
        elif move == "D":
            if now[1] == -5:
                continue
            else:
                road.add((now[0], now[1] - 1, now[0], now[1]))
                now =[now[0],now[1] - 1]
                
        elif move == "L":
            if now[0] == -5:
                continue
            else:
                road.add((now[0] - 1, now[1], now[0], now[1]))
                now =[now[0] - 1,now[1]]
                
        elif move == "R":
            if now[0] == 5:
                continue
            else:
                road.add((now[0], now[1], now[0] + 1, now[1]))
                now =[now[0] + 1,now[1]]
    
    return len(road)