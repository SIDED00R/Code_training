def check(start, end):
    if line[start] in ")}>]" or line[end] in "({[<":
        return 0
    if line[start] == "?" and line[end] == "?":
        return 4
    elif line[start] == "?" or line[end] == "?":
        return 1
    elif dic[line[start]] == line[end]:
        return 1
    else:
        return 0

line = input()
n = len(line)

dp = [[0 for _ in range(n)] for _ in range(n)]
dic = {"(": ")", "[": "]", "{" : "}", "<": ">"}

for i in range(n - 1):
    dp[i][i+1] = check(i, i+1)

for i in range(3, n, 2):
    for j in range(n - i):
        now_total = 0
        for k in range(j + 1, i + j + 1, 2):
            start = j
            end = k
            pair_count = check(start, end)

            if pair_count > 0:
                if k - 1 >= j + 1:
                    left_count = dp[j + 1][k - 1]
                else:
                    left_count = 1 
                if j + i >= k + 1:
                    right_count = dp[k + 1][i + j]
                else:
                    right_count = 1
                
                now_total += pair_count * left_count * right_count
        dp[j][j + i] = now_total

print(dp[0][n - 1])


