t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    line = list(map(int, input().split()))
    stack = []
    for _ in range(m):
        r, p = map(float, input().split())
        stack.append([r, p])
    stack = sorted(stack)
    
    now_idx = -1
    for idx in range(n - 1, -1, -1):
        if line[idx] != idx + 1:
            now_idx = idx + 1
            break
            
    if now_idx == -1:
        print(1)
    else:
        now_mul = 1
        answer = 0
        for now_case in stack:
            r, p = now_case
            if r < now_idx:
                continue
            answer += now_mul * p
            now_mul *= (1 - p)
        print(answer)