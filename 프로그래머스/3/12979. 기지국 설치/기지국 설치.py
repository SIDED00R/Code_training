import math
def solution(n, stations, w):
    now = 0
    answer = 0
    for station in stations:
        interval = station - now - w - 1
        answer += math.ceil(interval / (w * 2 + 1))
        now = station + w
    
    interval = n - now
    answer += math.ceil(interval / (w * 2 + 1))
    return answer