import sys
from collections import deque
input = sys.stdin.readline

N, D = map(int, input().split())
K = list(map(int, input().split()))

dp = [0] * N
dq = deque()
ans = -10**18

for i in range(N):
    while dq and dq[0] < i - D:
        dq.popleft()

    best_prev = dp[dq[0]] if dq else 0
    dp[i] = K[i] + max(0, best_prev)
    ans = max(ans, dp[i])

    while dq and dp[dq[-1]] <= dp[i]:
        dq.pop()
    dq.append(i)

print(ans)
