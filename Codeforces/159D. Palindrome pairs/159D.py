word = input()
length = len(word)
dp = [[0 for _ in range(length)] for _ in range(length)]

for i in range(length):
	dp[i][i] = 1
	
for i in range(1, length):
	if word[i - 1] == word[i]:
		dp[i - 1][i] = 1

for l in range(3, length):
	for i in range(length - l + 1):
		j = i + l - 1
		if word[i] == word[j] and dp[i + 1][j - 1]:
			dp[i][j] = 1
			
cnt_end = []
cnt_start = []
for i in range(length):
	end_sum = 0
	start_sum = 0
	for j in range(length):
		end_sum += dp[j][i]
		start_sum += dp[i][j]
	cnt_end.append(end_sum)
	cnt_start.append(start_sum)

left_sum = [0]
for i in range(length):
	left_sum.append(left_sum[-1] + cnt_end[i])
	
answer = 0
for i in range(1, length):
	answer += left_sum[i] * cnt_start[i]
print(answer)