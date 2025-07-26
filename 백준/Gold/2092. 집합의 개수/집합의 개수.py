from collections import defaultdict
t, a, s, b = map(int, input().split())
line = list(map(int, input().split()))
dic = defaultdict(int)

for num in line:
    dic[num] += 1

dp = [[0 for _ in range(a + 1)] for _ in range(t + 1)]
for idx in range(1, t + 1):
    for num in range(dic[idx] + 1):
        if idx == 1:
            dp[idx][num] = 1
            continue
        else:
            for j in range(num, a + 1):
                dp[idx][j] += dp[idx - 1][j - num]


print(sum(dp[-1][s:b + 1]) % 1000000)