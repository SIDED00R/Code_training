import heapq

stack = []
add_stack = []
n = int(input())
for _ in range(n):
    t, d = map(int, input().split())
    heapq.heappush(stack, [d, t, 0])

m = int(input())
for _ in range(m):
    w, t, d = map(int, input().split())
    heapq.heappush(add_stack, [w, d, t])

now_time = 0
while stack:
    if add_stack:
        next_time = add_stack[0][0]
        left_time = next_time - now_time
        while stack:
            d, t, _ = heapq.heappop(stack)
            if t > left_time:
                heapq.heappush(stack, [d, t - left_time, 0])
                now_time = next_time
                break
            else:
                now_time += t
                if now_time > d:
                    print('NO')
                    exit()
                left_time -= t
        if not stack:
            now_time = next_time
        while add_stack and now_time >= add_stack[0][0]:
            w, d, t = heapq.heappop(add_stack)
            heapq.heappush(stack, [d, t, 0])       
    else:
        d, t, _ = heapq.heappop(stack)
        now_time += t
        if now_time > d:
            print('NO')
            exit()

print('YES')
print(now_time)