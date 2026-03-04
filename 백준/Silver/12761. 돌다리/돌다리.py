from collections import deque
dp = [1e9 for _ in range(100001)]
a, b, n, m = map(int, input().split())
dp[n] = 1
stack = deque()
stack.append(n)
while stack:
    out = stack.popleft()
    if out >= a and dp[out - a] > dp[out] + 1:
        dp[out - a] = dp[out] + 1
        stack.append(out - a)
    if out >= b and dp[out - b] > dp[out] + 1:
        dp[out - b] = dp[out] + 1
        stack.append(out - b)
    if out >= 1 and dp[out - 1] > dp[out] + 1:
        dp[out - 1] = dp[out] + 1
        stack.append(out - 1)
    if out <= 100000 - 1 and dp[out + 1] > dp[out] + 1:
        dp[out + 1] = dp[out] + 1
        stack.append(out + 1)
    if out <= 100000 - a and dp[out + a] > dp[out] + 1:
        dp[out + a] = dp[out] + 1
        stack.append(out + a)
    if out <= 100000 - b and dp[out + b] > dp[out] + 1:
        dp[out + b] = dp[out] + 1
        stack.append(out + b)
    if out * a <= 100000 and dp[out * a] > dp[out] + 1:
        dp[out * a] = dp[out] + 1
        stack.append(out * a)
    if out * b <= 100000 and dp[out * b] > dp[out] + 1:
        dp[out * b] = dp[out] + 1
        stack.append(out * b)
    if dp[m] != 1e9:
        print(dp[m] - 1)
        break