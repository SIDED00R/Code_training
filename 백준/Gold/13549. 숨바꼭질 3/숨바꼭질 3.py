import sys
input = sys.stdin.readline
from math import inf
from collections import deque

N, K = map(int, input().rstrip('\n').split())
dp = [inf] * 100001
dp[N] = 0
stack = deque([N])

while True:
    now = stack.popleft()
    if now == K:
        print(dp[now])
        break
    count = dp[now]
    if now < 100000 and dp[now + 1] > count + 1:
        dp[now + 1] = count + 1
        stack.append(now + 1)
    if now > 0 and dp[now - 1] > count + 1:
        dp[now - 1] = count+ 1
        stack.append(now - 1)
    now *= 2
    while now <= 100000:
        if dp[now] > count:
            dp[now] = count
            stack.append(now)
            now *= 2
        else:
            break

