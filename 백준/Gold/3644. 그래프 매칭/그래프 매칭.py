try:
    while True:
        n = int(input())
        dp = [0] * (n + 1)
        if n == 3:
            print(4)
        elif n == 4:
            print(7)
        else:
            dp[2] = 2
            dp[3] = 3
            for idx in range(4, n + 1):
                dp[idx] = dp[idx - 1] + dp[idx - 2]
            
            print(dp[n] + dp[n - 2])
    
except:
    exit()