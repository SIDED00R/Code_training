def solution(n, times):
    find = False
    s, e = 1, 1e18
    while not find:
        print(s, e)
        total = 0
        mid = (s + e) // 2
        for time in times:
            total += mid // time
        if total >= n:
            e = mid
        else:
            s = mid
        if e - s == 1:
            return e