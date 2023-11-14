def dp(case):
    length = len(case)
    answer = [0] * length
    answer[0], answer[1] = case[0], max(case[0], case[1])
    for i in range(2, length):
        answer[i] = max(answer[i-1], answer[i-2] + case[i])
    return max(answer)

def solution(sticker):
    if len(sticker) < 3:
        return max(sticker)
    else:
        case1 = sticker[:-1]
        case2 = sticker[1:]

        return max(dp(case1),dp(case2))