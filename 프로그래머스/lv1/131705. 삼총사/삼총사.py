def solution(number):
    answer = 0
    for fidx, first in enumerate(number[:-2]):
        for sidx, second in enumerate(number[fidx + 1:-1]):
            for tidx, third in enumerate(number[fidx + sidx + 2:]):
                if first + second + third == 0:
                    answer += 1
    return answer