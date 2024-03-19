import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().rstrip('\n').split())

idx_count = defaultdict(int)
next_dic = defaultdict(list)
for _ in range(M):
    line = list(map(int, input().rstrip('\n').split()))
    for idx in range(1, len(line) - 1):
        first = line[idx]
        second = line[idx + 1]
        idx_count[second] += 1
        next_dic[first].append(second)

answer = []     
stack = []
for i in range(1, N + 1):
    if i not in idx_count:
        stack.append(i)
      
next_stack = []
while stack:
    now = stack.pop()
    answer.append(now)
    for case in next_dic[now]:
        idx_count[case] -= 1
        if idx_count[case] == 0:
            next_stack.append(case)
    if not stack:
        stack = next_stack[:]
        next_stack = []
     
if len(answer) != N:
    print(0)
else:
    for num in answer:
        print(num)
        