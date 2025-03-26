def solution(n, w, num):
    ans_list = []
    start = num
    while not 1 <= start <= 2 * w:
        start -= 2 * w
    
    if 1 <= start <= w:
        start = num
    else:
        dt = 2 * w - num
        start = dt + 1
    second = 2 * w - start + 1
    
    while start <= n:
        if start < num:
            start += 2 * w
            continue
        ans_list.append(start)
        start += 2 * w
        
    while second <= n:
        if second < num:
            second += 2 * w
            continue
        ans_list.append(second)
        second += 2 * w
        
    return len(ans_list)
