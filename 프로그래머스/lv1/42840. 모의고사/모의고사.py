def solution(answers):
    c1, c2, c3 = 0, 0, 0
    for idx, num in enumerate(answers):
        if idx % 5 + 1 == num:
            c1 += 1
        if idx % 2 == 0 and num == 2:
            c2 += 1
        elif idx % 2 != 0 and [1, 3, 4, 5][(idx % 8 - 1) // 2] == num:
            c2 += 1
        if [3, 1, 2, 4, 5][(idx % 10) // 2] == num:
            c3 += 1
    l = [c1, c2, c3]
    if l.count(max(l)) == 3:
        return [1,2,3]
    elif l.count(max(l)) == 2:
        return [1,2,3][:l.index(min(l))] + [1,2,3][l.index(min(l)) + 1:]
    return [l.index(max(l)) + 1]