def solution(array):
    idx = 0
    num = 0
    for i, n in enumerate(array):
        if n > num:
            num = n
            idx = i
    return [num, idx]