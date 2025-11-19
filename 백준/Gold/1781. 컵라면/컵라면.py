import heapq

n = int(input())
stack = []
for _ in range(n):
    dead, cup = map(int, input().split())
    heapq.heappush(stack, [-dead, cup])

answer = 0
keep = []
while stack:
    dead, cup = heapq.heappop(stack)
    heapq.heappush(keep, -cup)
    while stack and stack[0][0] == dead:
        dead, cup = heapq.heappop(stack)
        heapq.heappush(keep, -cup)

    if stack:
        for _ in range(stack[0][0] - dead):
            if keep:
                out = heapq.heappop(keep)
                answer -= out
            else:
                break
    else:
        for _ in range(-dead):
            if keep:
                out = heapq.heappop(keep)
                answer -= out
            else:
                break

print(answer)