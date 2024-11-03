import heapq

n = int(input())
stack = []
for _ in range(n):
    l, r = map(int, input().split())
    heapq.heappush(stack, [l, r])

start, end = 0, 0
bridge = []
while stack:
    l, r = heapq.heappop(stack)
    if l <= end:
        end = max(end, r)
    else:
        bridge.append([start, end])
        start = l
        end = r
bridge.append([start, end])

reachable = 0
answer = 0
for now_bridge in bridge:
    l, r = now_bridge
    if reachable < l:
        break
    length = r - l
    reachable = max(reachable, r + length)
    answer = max(answer, r)
print(answer)