n = int(input())
line = list(map(int, input().split()))
chair = []
non_chair = []
for i in range(len(line)):
	if line[i]:
		chair.append(i)
	else:
		non_chair.append(i)
		
c = len(chair)
nc = len(non_chair)

if c == 0:
	print(0)
	exit()

dp = [[0 for _ in range(nc)] for _ in range(c)]

dp[0][0] = abs(chair[0] - non_chair[0])
for i in range(1, nc):
	dp[0][i] = min(dp[0][i - 1], abs(chair[0] - non_chair[i]))

for i in range(1, c):
	for j in range(i, nc):
		if i == j:
			dp[i][j] = dp[i - 1][j - 1] + abs(chair[i] - non_chair[j])
		else:
			dp[i][j] = min(dp[i - 1][j - 1] + abs(chair[i] - non_chair[j]), dp[i][j - 1])
		
print(dp[-1][-1])