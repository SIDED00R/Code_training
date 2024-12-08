from collections import deque

n = int(input())
value = [0]
for _ in range(n):
    value.append(int(input()))

answer = 0
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
stack = deque([[1, n]])
while stack:
    start, end = stack.popleft()
    if start == end:
        answer = max(dp[start][end] + n * value[start], answer)
        continue
    if dp[start][end] + (n - end + start) * value[start] > dp[start + 1][end]:
        dp[start + 1][end] = dp[start][end] + (n - end + start) * value[start]
        stack.append([start + 1, end])
    if dp[start][end] + (n - end + start) * value[end] > dp[start][end - 1]:
        dp[start][end - 1] = dp[start][end] + (n - end + start) * value[end]
        stack.append([start, end - 1])

print(answer)




    