from itertools import permutations
from collections import deque

n = int(input())
start_list = list(map(int, input().split()))
answer_list = sorted(start_list)
m = int(input())
move_stack = []
for _ in range(m):
    l, r, c = map(int, input().split())
    move_stack.append([l - 1, r - 1, c])

total_dic = {}
for now_case in permutations(start_list, n):
    total_dic[now_case] = -1

total_dic[tuple(start_list)] = 0
now_stack = deque([start_list])
while now_stack:
    now_line = now_stack.popleft()
    now_cost = total_dic[tuple(now_line)]
    for move_case in move_stack:
        l, r, c = move_case
        next_line = now_line[:]
        next_line[l], next_line[r] = next_line[r], next_line[l]
        if total_dic[tuple(next_line)] == -1:
            total_dic[tuple(next_line)] = now_cost + c
            now_stack.append(next_line)
        elif total_dic[tuple(next_line)] > now_cost + c:
            total_dic[tuple(next_line)] = now_cost + c
            now_stack.append(next_line)

print(total_dic[tuple(answer_list)])
        