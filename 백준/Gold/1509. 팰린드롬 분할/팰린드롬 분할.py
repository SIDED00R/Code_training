import sys
input = sys.stdin.readline

line = list(input().strip())
add_line = ['.']
for alp in line:
    add_line.append(alp)
    add_line.append('.')

pal_num = []
n = len(add_line)
for idx in range(n):
    length = 0
    while True:
        length += 1
        front = idx - length
        back = idx + length
        if front >= 0 and back < n:
            if add_line[front] == add_line[back]:
                continue
            else:
                break
        else:
            break
    pal_num.append(length - 1)

dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1
    for j in range(i):
        if pal_num[j] + j + 1 >= i and (2 * (j + 1) >= i):
            dp[i] = min(dp[i], dp[2 * (j + 1) - i] + 1)

print(dp[-1] - 1)