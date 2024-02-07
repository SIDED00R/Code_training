def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10
    n = len(onboard)
    dp = [[1e9 for _ in range(51)] for _ in range(n + 1)]
    now = temperature
    able_temperature = set([now])
    dp[0][now] = 0
    for i, case in enumerate(onboard):
        idx = i + 1
        next_temperature = set()
        for now in able_temperature:
            hot = temperature - now
            if case:
                if t1 <= now <= t2:
                    # turn off
                    if hot > 0:
                        dp[idx][now + 1] = min(dp[idx - 1][now], dp[idx][now + 1])
                        next_temperature.add(now + 1)
                    elif hot < 0:
                        dp[idx][now - 1] = min(dp[idx - 1][now], dp[idx][now - 1]) 
                        next_temperature.add(now - 1)
                    else:
                        dp[idx][now] = min(dp[idx - 1][now],  dp[idx][now])
                        next_temperature.add(now)
                
                    # turn on
                    if now != 0:
                        dp[idx][now - 1] = min(dp[idx - 1][now] + a, dp[idx][now - 1])
                        next_temperature.add(now - 1)
                    if now != 50:
                        dp[idx][now + 1] = min(dp[idx - 1][now] + a, dp[idx][now + 1])
                        next_temperature.add(now + 1)
                    dp[idx][now] = min(dp[idx - 1][now] + b, dp[idx][now])
                    next_temperature.add(now)
            else:
                # turn off
                if hot > 0:
                    dp[idx][now + 1] = min(dp[idx - 1][now], dp[idx][now + 1])
                    next_temperature.add(now + 1)
                elif hot < 0:
                    dp[idx][now - 1] = min(dp[idx - 1][now], dp[idx][now - 1]) 
                    next_temperature.add(now - 1)
                else:
                    dp[idx][now] = min(dp[idx - 1][now],  dp[idx][now])
                    next_temperature.add(now)
                
                # turn on
                if now != 0:
                    dp[idx][now - 1] = min(dp[idx - 1][now] + a, dp[idx][now - 1])
                    next_temperature.add(now - 1)
                if now != 50:
                    dp[idx][now + 1] = min(dp[idx - 1][now] + a, dp[idx][now + 1])
                    next_temperature.add(now + 1)
                dp[idx][now] = min(dp[idx - 1][now] + b, dp[idx][now])
                next_temperature.add(now)
                
        able_temperature = next_temperature.copy()

    return min(dp[-1])