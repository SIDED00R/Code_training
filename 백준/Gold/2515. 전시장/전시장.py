def find(hight, n):
    first = 0
    last = n
    while first <= last:
        mid = (first + last) // 2
        if stack[mid][0] > hight:
            last = mid - 1
        else:
            first = mid + 1
    return last

n, s = map(int, input().split())
stack = []
for _ in range(n):
    h, c = map(int, input().split())
    stack.append([h, c])
stack = sorted(stack, key = lambda x: [x[0], -x[1]])

dp = [0] * (n + 1)
dp[0] = [0, 0]
for i in range(n):
    dp[i + 1] = dp[i][:]
    if s > stack[i][0]:
        continue
    if stack[i][0] - dp[i + 1][0] >= s:
        dp[i + 1] = [stack[i][0], dp[i + 1][1] + stack[i][1]]
    else:
        idx = find(stack[i][0] - s, n)
        if idx == -1:
            if dp[i + 1][1] < stack[i][1]:
                dp[i + 1] = [stack[i][0], stack[i][1]]
        else:
            if dp[i + 1][1] < stack[i][1] + dp[idx + 1][1]:
                dp[i + 1] = [stack[i][0], stack[i][1] + dp[idx + 1][1]]

print(dp[-1][1])