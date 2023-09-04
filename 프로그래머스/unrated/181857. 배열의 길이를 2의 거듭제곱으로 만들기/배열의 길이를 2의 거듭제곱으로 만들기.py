def solution(arr):
    length = len(arr)
    for i in range(11):
        if length > 2**i:
            continue
        else:
            n = 2**i - length
            for _ in range(n):
                arr.append(0)
            return arr