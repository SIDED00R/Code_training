from collections import deque

n, k = map(int, input().split())

weight = [[1e10, 1e10] for _ in range(500001)]
weight[n] = [0, 1e10]
stack = deque()
stack.append([n, 0])

while stack:
    out, sign = stack.popleft()
    next_weight = weight[out][sign] + 1
    if out - 1 >= 0 and weight[out - 1][(sign + 1) % 2] > next_weight:
        weight[out - 1][(sign + 1) % 2] = next_weight
        stack.append([out - 1, (sign + 1) % 2])
    if out + 1 <= 500000 and weight[out + 1][(sign + 1) % 2] > next_weight:
        weight[out + 1][(sign + 1) % 2] = next_weight
        stack.append([out + 1, (sign + 1) % 2])
    if out * 2 <= 500000 and weight[out * 2][(sign + 1) % 2] > next_weight:
        weight[out * 2][(sign + 1) % 2] = next_weight
        stack.append([out * 2, (sign + 1) % 2])

answer = 1e10
now_k = k
for i in range(500000):
    now_k += i
    if now_k > 500000:
        break
    now_weight = weight[now_k][i % 2]
    if i < now_weight:
        continue
    else:
        print(i)
        exit()
print(-1)
