num = input()
length = len(num)
dp = [0 for _ in range(length)]
if num[0] == "0":
    print(0)
    exit()
else:
    dp[0] = 1
for idx in range(1, length):
    if num[idx] != "0":
        dp[idx] += dp[idx - 1]
    if idx == 1:
        now_num = int(num[:2])
        if 10 <= now_num <= 26:
            dp[1] += 1
    else:
        now_num = int(num[idx - 1:idx + 1])
        if 10 <= now_num <= 26:
            dp[idx] += dp[idx - 2]
    dp[idx] %= 1000000

print(dp[-1])