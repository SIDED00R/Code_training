n = int(input())
length = [0]
while True:
    now_num = int(input())
    if now_num == 0 or now_num > n * 100:
        break
    length.append(now_num)

dp = [[0 for _ in range(n * 100 + 1)] for _ in range(len(length) + 1)]

total = 0
for i in range(1, len(length)):
    now_num = length[i]
    if total <= n * 100:
        dp[i][now_num] = 1
    total += now_num
    for j in range(100, n * 100 + 1):
        if dp[i - 1][j] != 0:
            if j + now_num <= n * 100:
                dp[i][j + now_num] = max(dp[i - 1][j] + 1, dp[i][j + now_num])
            if total - j <= n * 100:
                dp[i][j] = max(dp[i - 1][j], dp[i][j])

last = []
for i in range(len(dp)):
    for j in range(len(dp[0])):
        if dp[i][j] != 0:
            last.append([i, j, dp[i][j]])

if not last:
    print(0)
    exit()
now_idx, now_total, now_count = last.pop()
answer_count = now_idx
answer = []
while True:
    weight = length[now_idx]
    if now_count == 1:
        if weight == now_total:
            answer.append(now_idx)
            break
        else:
            now_idx -= 1
            continue

    if now_total >= weight and dp[now_idx - 1][now_total - weight] == now_count - 1:
        answer.append(now_idx)
        now_idx -= 1
        now_total -= weight
        now_count -= 1

    else:
        now_idx -= 1

answer_list = ["port"] * answer_count
for answer_idx in answer:
    answer_list[answer_idx - 1] = "starboard"

print(answer_count)
for word in answer_list:
    print(word)