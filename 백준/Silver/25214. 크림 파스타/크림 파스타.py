n = int(input())
line = list(map(int, input().split()))

min_val = line[0]
answer = [0]

for i in range(1, n):
    diff = line[i] - min_val
    max_diff = max(answer[-1], diff)
    answer.append(max_diff)
    min_val = min(min_val, line[i])

print(' '.join(map(str, answer)))
