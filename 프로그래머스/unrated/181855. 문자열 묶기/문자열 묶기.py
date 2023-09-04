def solution(strArr):
    answer = [len(i) for i in strArr]
    num = sorted(set(answer))
    mx = 0
    for n in num:
        c = answer.count(n)
        if c >= mx:
            mx = c
    return mx