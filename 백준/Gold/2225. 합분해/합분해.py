n, k = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(k)]

for j in range(n + 1):
	dp[0][j] = 1

for i in range(1, k):
	for j in range(n + 1):
		for k in range(j + 1):
			dp[i][j] += dp[i - 1][j - k]
			dp[i][j] %= 1000000000
			
print(dp[-1][-1])
		
