from collections import defaultdict, deque

n, g = map(int, input().split())
count_line = []
lines = []
dic = defaultdict(list)
for idx in range(g):
    line = list(map(int, input().split()))
    count_line.append(line[0])
    lines.append(line[1:])
    for num in line[1:]:
        dic[num].append(idx)

stack = deque([1])
answer = set()
while stack:
    now = stack.popleft()
    before_length = len(answer)
    answer.add(now)
    after_length = len(answer)
    if before_length != after_length:
        for idx in dic[now]:
            count_line[idx] -= 1
            if count_line[idx] == 1:
                stack.extend(lines[idx])

print(len(answer))




        

