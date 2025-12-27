import heapq

n = int(input())
stack = []
for _ in range(n):
    t, s = map(int, input().split())
    heapq.heappush(stack, [s, t])

answer = stack[0][0] - stack[0][1]
now_time = answer
while stack:
    s, t = heapq.heappop(stack)
    now_time += t
    if now_time > s:
        diff = now_time - s
        answer -= diff
        now_time = s

if answer < 0:
    print(-1)
else:
    print(answer)