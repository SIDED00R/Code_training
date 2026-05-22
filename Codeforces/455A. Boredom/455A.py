from collections import Counter
n = int(input())
line_dic = Counter(map(int, input().split()))
num_list = []
for k, v in line_dic.items():
    num_list.append([k, v * k])
num_list = sorted(num_list)

dp = [[0, 0] for _ in range(len(num_list))]
dp[0] = [0, num_list[0][1]]

for idx in range(1, len(num_list)):
    if num_list[idx][0] - 1 == num_list[idx - 1][0]:
    	dp[idx] = [max(dp[idx - 1]), dp[idx - 1][0] + num_list[idx][1]]
    else:
        dp[idx] = [max(dp[idx - 1]), max(dp[idx - 1]) + num_list[idx][1]]

print(max(dp[-1]))