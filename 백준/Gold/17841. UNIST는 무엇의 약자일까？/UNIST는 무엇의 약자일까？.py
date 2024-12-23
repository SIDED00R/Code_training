n = int(input())
dp = [[0 for _ in range(5)] for _ in range(n + 1)]
for i in range(1, n + 1):
    letter = input()
    dp[i] = dp[i - 1][:]

    if letter[:1] == "U":
        dp[i][0] += 1
    if letter[:2] == "UN":
        dp[i][1] += 1
    if letter[:3] == "UNI":
        dp[i][2] += 1
    if letter[:4] == "UNIS":
        dp[i][3] += 1
    if letter[:5] == "UNIST":
        dp[i][4] += 1

    if letter[:1] == "N":
        dp[i][1] += dp[i - 1][0]
    if letter[:2] == "NI":
        dp[i][2] += dp[i - 1][0]
    if letter[:3] == "NIS":
        dp[i][3] += dp[i - 1][0]
    if letter[:4] == "NIST":
        dp[i][4] += dp[i - 1][0]

    if letter[:1] == "I":
        dp[i][2] += dp[i - 1][1]
    if letter[:2] == "IS":
        dp[i][3] += dp[i - 1][1]
    if letter[:3] == "IST":
        dp[i][4] += dp[i - 1][1]

    if letter[:1] == "S":
        dp[i][3] += dp[i - 1][2]
    if letter[:2] == "ST":
        dp[i][4] += dp[i - 1][2]

    if letter[:1] == "T":
        dp[i][4] += dp[i - 1][3]

print(dp[-1][-1] % 1000000007)
