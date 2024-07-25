from collections import deque

n = int(input())
nodes = deque([])
for _ in range(n):
    nodes.append(list(map(int, input().split())))
   
now_time = 0
while nodes:
    a, b = nodes.popleft()
    left_time = now_time % (a + b)
    if left_time >= b:
        now_time += 1
    else:
        now_time += 1 + b - left_time
        
print(now_time)