n, d = map(int, input().split())
stack = []
for _ in range(n):
    m, s = map(int, input().split())
    stack.append([m, s])
    
sorted_stack = sorted(stack)
answer = 0
now_count = 0
before_idx = 0
for now_case in sorted_stack:
    m, s = now_case
    now_count += s
    while m - sorted_stack[before_idx][0] >= d:
        now_count -= sorted_stack[before_idx][1]
        before_idx += 1
    answer = max(answer, now_count)
    
print(answer)