from collections import defaultdict
import heapq

dic = defaultdict(int)
stack = []
n = int(input())
for _ in range(n):
    inp = int(input())
    heapq.heappush(stack, -inp)
    dic[inp] += 1

g = stack[0]
while stack[0] == g:
    heapq.heappop(stack)

s = stack[0]
while stack[0] == s:
    heapq.heappop(stack)

print(-stack[0], dic[-stack[0]])