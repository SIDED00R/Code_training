def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_idx = []
    pick_idx = []
    d = 0
    p = 0
    for i in range(n):
        deliver = deliveries.pop()
        pick = pickups.pop()
        
        # 배달
        if d == 0:
            if deliver != 0:
                d += deliver
                deliver_idx.append(n - i)
        else:
            if deliver != 0:
                d += deliver
        #수거
        if p == 0:
            if pick != 0:
                p += pick
                pick_idx.append(n - i)
        else:
            if pick != 0:
                p += pick
        
        #같은장소 여러번
        while d > cap:
            d -= cap
            deliver_idx.append(n - i)
        if d == cap:
            d = 0
        
        while p > cap:
            p -= cap
            pick_idx.append(n - i)
        if p == cap:
            p = 0
            
    dl = len(deliver_idx)
    pl = len(pick_idx)
    if pl > dl:
        for i in range(dl):
            answer += max(deliver_idx[i], pick_idx[i])
        answer += sum(pick_idx[dl:])
    else:
        for j in range(pl):
            answer += max(deliver_idx[j], pick_idx[j])
        answer += sum(deliver_idx[pl:])
        
    return answer * 2