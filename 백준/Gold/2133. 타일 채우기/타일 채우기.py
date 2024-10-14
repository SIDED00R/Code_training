def total(num):
    ans = 0
    for i in range(0, num + 1 , 2):
        ans += dp[i] * 2
    ans += dp[num - 2]
    return ans

n = int(input())
if n % 2 == 1:
    print(0)
    exit()
dp = [0] * 31
dp[0] = 1
dp[2] = 3
for idx in range(4, n + 1, 2):
    dp[idx] = total(idx)
print(dp[n])