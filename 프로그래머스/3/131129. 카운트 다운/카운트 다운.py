from collections import defaultdict

def solution(target):
    count = 0
    while target > 600:
        target -= 60
        count += 1
    dic = defaultdict(int)
    for num in range(1, 21):
        for mul in range(1, 4):
            if mul == 1:
                dic[num * mul] = 1
            else:
                dic[num * mul] = 0
    dic[50] = 1
    
    dp = [[2000, 0] for _ in range(target + 1)]
    dp[0] = [0, 0]
    for idx in range(target + 1):
        now = dp[idx]
        for key, value in dic.items():
            if idx + key <= target:
                check = dp[idx + key]
                if now[0] + 1 < check[0] or (now[0] + 1 == check[0] and now[1] + value > check[1]):
                    dp[idx + key] = [now[0] + 1, now[1] + value]
    dp[target][0] += count               
    return dp[target]