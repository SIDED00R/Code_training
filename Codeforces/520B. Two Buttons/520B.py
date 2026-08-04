n, m = map(int, input().split())
dp = [-1 for _ in range(2 * (max(n, m)))]
dp[n] = 0
stack = [n]
while dp[m] == -1:
    next_stack = []
    for now_num in stack:
        num = dp[now_num]
        if now_num - 1 >= 0 and dp[now_num - 1] == -1:
            dp[now_num - 1] = num + 1
            next_stack.append(now_num - 1)
        if now_num * 2 < 2 * m and dp[now_num * 2] == -1:
            dp[now_num * 2] = num + 1
            next_stack.append(now_num * 2)
    stack = next_stack[:]
        
print(dp[m])