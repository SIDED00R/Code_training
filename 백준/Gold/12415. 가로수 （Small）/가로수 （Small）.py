t = int(input())
for case in range(t):
    n, m, b = map(int, input().split())
    answer = 0
    
    power = {}
    for _ in range(m):
        p, q = map(int, input().split())
        power[p] = q

    stack = []
    for k1, v1 in power.items():
        if k1 >= b:
            stack.append([k1, k1, 0])
            continue
        for k2, v2 in power.items():
            stack.append([k1 + k2, k1, k2])
    sort_stack = sorted(stack)
    for now_case in sort_stack:
        total_w, first, second = now_case
        if total_w < b:
            continue
        if second == 0:
            if n <= power[first]:
                answer += first * n
                n = 0
            else:
                n -= power[first]
                answer += first * power[first] 
                power[first] = 0

        elif first == second:
            if n <= power[first] // 2:
                answer += total_w * n
                n = 0
            else:
                n -= power[first] // 2
                answer += total_w * (power[first] // 2)
                power[first] -= (power[first] // 2) * 2
        else:
            min_count = min(power[first], power[second])
            if n <= min_count:
                answer += total_w * n
                n = 0
            else:
                n -= min_count
                answer += total_w * min_count
                power[first] -= min_count
                power[second] -= min_count
        
        if n == 0:
            break

    if n != 0:
        answer = -1    
    print(f"Case #{case + 1}: {answer}")