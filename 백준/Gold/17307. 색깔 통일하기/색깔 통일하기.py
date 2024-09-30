import sys

n, c = map(int, input().split())
button = list(map(int, list(sys.stdin.readline().split())))
if n == 1:
    print(1)
    print(0)
    exit()

weights = []
weights.append([0, (button[1] - button[0]) % c])
for idx in range(1, len(button) - 1):
    weights.append([(button[idx - 1] - button[idx]) % c, (button[idx + 1] - button[idx]) % c])
weights.append([(button[-2] - button[-1]) % c, 0])

total_r = 0
total_l = 0
for l, r in weights:
    total_r += r

answer = total_r
answer_idx = 1
for idx in range(1, len(weights) - 1):
    l = weights[idx][0]
    r = weights[idx - 1][1]
    total_l += l
    total_r -= r
    if answer != min(answer, max(total_l, total_r)):
        answer_idx = idx + 1
        answer = min(answer, max(total_l, total_r))
    if total_l >= total_r:
        break

print(answer_idx)
print(answer)