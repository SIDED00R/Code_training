from collections import deque

dic = {i:deque() for i in range(10)}

n = int(input())
if n == 0:
    print(0)
    exit()
line = list(map(int, input().split()))
for idx, num in enumerate(line):
    dic[num].append(idx)

for num in range(10):
    dic[num].append(n)

answer = 0
stack = []
for num in line:
    dic[num].popleft()
    if num in stack:
        continue
    if len(stack) < 4:
        answer += 1
        stack.append(num)
    else:
        max_value = 0
        out = -1
        for out_case in stack:
            idx = dic[out_case][0]
            if idx > max_value:
                max_value = idx
                out = out_case
        stack.remove(out)
        stack.append(num)
        answer += 1

print(answer)