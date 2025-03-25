from collections import defaultdict
import heapq

dic = defaultdict(int)
stack = set()
n = int(input())
for _ in range(n):
    inp = int(input())
    stack.add(inp)
    dic[inp] += 1

stack = sorted(list(stack))
print(stack[-3], dic[stack[-3]])