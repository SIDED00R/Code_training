def solution(n, cores):
    if len(cores) >= n:
        return 0
    
    max_time = 50000 * 10000 + 1
    min_time = 0
    find = True
    while min_time + 1 < max_time:
        total = 0
        mid_time = (max_time + min_time) // 2
        for core in cores:
            total += (mid_time // core) + 1
        if total >= n:
            max_time = mid_time
        else:
            min_time = mid_time
            
    count = 0
    able = []
    for idx, core in enumerate(cores):
        count += (max_time // core) + 1
        if max_time % core == 0:
            able.append(idx)
    left = count - n
    return able[-(left + 1)] + 1