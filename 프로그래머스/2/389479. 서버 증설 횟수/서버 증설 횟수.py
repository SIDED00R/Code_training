def solution(players, m, k):
    answer = 0
    now_server = [0] * 24
    for idx, p in enumerate(players):
        s = p // m
        keep = now_server[idx]
        answer += max(0, s - now_server[idx])
        for i in range(k):
            if idx + i < 24:
                now_server[idx + i] += max(s - keep, 0)
                
    return answer