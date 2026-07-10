def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    part = gcd(a, b)
    return a * b // part

def solution(signals):
    answer = -1
    limit = 1
    check = []
    for signal in signals:
        g, y, r = signal
        limit = lcm(limit, g + y + r)
        check.append([g + y + r, g + 1, g + y])
    
    for num in range(1, limit + 1):
        find = True
        for now_case in check:
            total, start, end = now_case
            if not start <= (num - 1) % total + 1 <= end:
                find = False
        if find:
            answer = num
            break
            
    return answer