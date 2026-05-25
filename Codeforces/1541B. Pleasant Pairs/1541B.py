t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    weight = [0] * (2 * n + 1)
    for idx, num in enumerate(line):
        weight[num] = idx + 1
    answer = 0
    for i in range(1, 2 * n + 1):
        now_num = weight[i]
        if now_num == 0:
            continue
        for j in range(1, 2 * n // i + 1):
            if weight[j] == 0 or weight[i] >= weight[j]:
                continue
            if i * j == weight[i] + weight[j]:
                answer += 1
    print(answer)