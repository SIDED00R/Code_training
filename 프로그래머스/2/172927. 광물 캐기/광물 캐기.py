def solution(picks, minerals):
    arr = []
    answer = 0
    for i in range(0, min(len(minerals), sum(picks) * 5), 5):
        case = minerals[i:i + 5]
        arr.append([case.count("diamond"), case.count("iron"), case.count("stone")])
    arr = sorted(arr, key = lambda x: [x[0], x[1], x[2]])
    while arr != []:
        d, i, s = arr.pop()
        if picks[0] != 0:
            picks[0] -= 1
            answer += d + i + s
        elif picks[1] != 0:
            picks[1] -= 1
            answer += 5 * d + i + s
        elif picks[2] != 0:
            picks[2] -= 1
            answer += 25 * d + 5 * i + s
    return answer