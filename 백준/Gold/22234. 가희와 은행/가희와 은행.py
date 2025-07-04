from collections import deque

already_list = []
after_list = []
n, time, w = map(int, input().split())
for _ in range(n):
    p, t = map(int, input().split())
    already_list.append([0, p, t])

m = int(input())
for _ in range(m):
    p, t, c = map(int, input().split())
    after_list.append([c, p, t])

after_list = sorted(after_list)

already_list = deque(already_list)
after_list = deque(after_list)

total_time = 0
answer = []
while True:
    if total_time >= w:
        break
    _, p, t = already_list.popleft()
    back = False
    if t <= time:
        total_time += t
        for _ in range(t):
            answer.append(p)
    else:
        total_time += time
        for _ in range(time):
            answer.append(p)
        back = True
    while after_list and after_list[0][0] <= total_time:
        now_out = after_list.popleft()
        already_list.append(now_out)
    if back:
        already_list.append([0, p, t - time])

for num in answer[:w]:
    print(num)