t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    for idx in range(n):
        max_weight = 0
        for j in range(idx):
            if line[idx] >= line[j]:
                max_weight = max(max_weight, dp[j])
        dp[idx] = max_weight + line[idx]

    total = sum(line)
    print(total - max(dp))
        