def solution(common):
    if sum(common[:3]) == common[1] * 3:
        return common[-1] + (common[1] - common[0])
    return common[-1] * (common[1] // common[0])