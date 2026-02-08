from collections import deque

tri = [0]
for i in range(1, 122):
    tri.append(tri[-1] + i)

four = [0]
for num in tri[1:]:
    four.append(four[-1] + num)
n = int(input())
dp = [1e10] * (n + 1)
stack = deque(four[:])

for num in four:
    if num <= n:
        dp[num] = 1
    else:
        break
while stack:
    out = stack.popleft()
    for num in four[1:]:
        if out + num <= n and dp[out + num] == 1e10:
            stack.append(out + num)
            dp[out + num] = dp[out] + 1

print(dp[-1])