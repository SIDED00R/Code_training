import sys
input = sys.stdin.readline
from collections import defaultdict

answer = []
N, M = map(int, input().rstrip('\n').split())
count_dic = defaultdict(int)
next_dic = defaultdict(list)
for _ in range(M):
    front, back = map(int, input().rstrip('\n').split())
    count_dic[back] += 1
    next_dic[front].append(back)
    
stack = []
for i in range(1, N + 1):
    if i not in count_dic:
        stack.append(i)
      
next_stack = []
while stack:
    now = stack.pop()
    answer.append(now)
    for case in next_dic[now]:
        count_dic[case] -= 1
        if count_dic[case] == 0:
            next_stack.append(case)
    if not stack:
        stack = next_stack[:]
        next_stack = []
        
for num in answer:
    print(num, end = " ")
