def solution(d, budget):
    little = sorted(d)
    add = 0
    count = 0
    for i in little:
        if add + i > budget:
            return count
        else:
            add += i
            count += 1
    return count