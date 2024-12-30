from collections import defaultdict
import heapq

n = int(input())
events = []
for _ in range(n):
    a, b, h = map(int, input().split())
    events.append((a, h, 1)) 
    events.append((b, h, -1)) 
events.sort()

active_heights = defaultdict(int)
prev_x = 0
prev_max_height = 0
area = 0
height_stack = []

for x, h, event_type in events:
    if x != prev_x:
        area += (x - prev_x) * prev_max_height
        prev_x = x

    if event_type == 1:
        active_heights[h] += 1
        heapq.heappush(height_stack, -h)
        prev_max_height = max(prev_max_height, h)
    else: 
        active_heights[h] -= 1
        if active_heights[h] == 0:
            del active_heights[h]
            if h == prev_max_height:
                while -height_stack[0] not in active_heights:
                    heapq.heappop(height_stack)
                    if height_stack:
                        prev_max_height = -height_stack[0]
                        continue
                    else:
                        prev_max_height = 0
                        break

print(area)
