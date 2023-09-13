def solution(t, p):
    answer = 0
    for n in range(len(t) - len(p) + 1):
        if t[n:n + len(p)] > p:
            continue
        else:
            answer += 1
    return answer