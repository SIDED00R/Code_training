n = int(input())
dp = [0 for _ in range(n + 1)]
dp[1] = [0, [1]]
now_stack = [1]
count = 0
not_find = True
while not_find:
    next_stack = []
    for num in now_stack:
        if num + 1 <= n and dp[num + 1] == 0:
            dp[num + 1] = [count + 1, dp[num][1] + [num + 1]]
            next_stack.append(num + 1)
        if num * 2 <= n and dp[num * 2] == 0:
            dp[num * 2] = [count + 1, dp[num][1] + [num * 2]]
            next_stack.append(num * 2)
        if num * 3 <= n and dp[num * 3] == 0:
            dp[num * 3] = [count + 1, dp[num][1] + [num * 3]]
            next_stack.append(num * 3)
    if dp[n] == 0:
        now_stack = next_stack[:]
        count += 1
        continue
    else:
        break

print(dp[n][0])
for num in dp[n][1][::-1]:
    print(num, end = " ")
    
 