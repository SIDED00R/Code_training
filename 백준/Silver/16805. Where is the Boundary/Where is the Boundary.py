import sys
n, m = map(int, input().split())
count_w = [0] * (n + 1)
count_e = [0] * (n + 1)
for i in range(m):
    line = sys.stdin.readline().rstrip('\n')
    now_e = 0
    now_w = 0
    for idx in range(len(line)):
        if line[idx] == "E":
            now_w += 1
        count_w[idx + 1] += now_w
    for idx in range(1, len(line) + 1):
        if line[-idx] == "W":
            now_e += 1
        count_e[-idx - 1] += now_e

total = n * m
answer = n
for idx in range(n + 1):
    if total > count_w[idx] + count_e[idx]:
        total = count_w[idx] + count_e[idx]
        answer = idx

print(answer, answer + 1)