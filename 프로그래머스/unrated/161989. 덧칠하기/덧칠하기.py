def solution(n, m, section):
    answer = 0
    while len(section) != 0:
        last = section.pop()
        while len(section) != 0 and section[-1] > last - m:
            section.pop()
        answer += 1
    return answer