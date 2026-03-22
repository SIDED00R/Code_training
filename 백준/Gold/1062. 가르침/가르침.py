from itertools import combinations
from collections import defaultdict
import copy

alp_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
base_set = set("antaica")

n, k = map(int, input().split())
if k < 5:
    print(0)
    exit()
keep_stack = []
for _ in range(n):
    s = set(input())
    keep_stack.append(s)

answer = 0
for now_case in combinations(alp_list, k - 5):
    now_set = copy.deepcopy(base_set)
    now_answer = 0
    for alp in now_case:
        now_set.add(alp)
    for now_keep in keep_stack:
        find = True
        for alp in now_keep:
            if alp not in now_set:
                find = False
                break
        if find:
            now_answer += 1
    answer = max(answer, now_answer)

print(answer)