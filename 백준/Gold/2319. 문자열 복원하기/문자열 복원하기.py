from collections import defaultdict
import copy

n, l, m = map(int, input().split())
line = list(input().split())

next_dic = defaultdict(list)
start = defaultdict(int)
for now_case in line:
    if len(now_case) == 1:
        print(m ** l)
        exit()
    elif l < len(now_case):
        print(n ** l)
        exit()
    else:
        next_dic[now_case[:-1]].append(now_case[-1])
        start[now_case[1:]] += 1

for _ in range(l - len(line[0])):
    next_start = defaultdict(int)
    for k, v in start.items():
        if k in next_dic:
            for next_alp in next_dic[k]:
                next_start[k[1:] + next_alp] += v
    start = copy.deepcopy(next_start)

answer = 0
for _, v in start.items():
    answer += v

print(answer)