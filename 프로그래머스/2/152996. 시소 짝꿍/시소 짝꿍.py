from collections import Counter

def solution(weights):
    dic = Counter(weights)
    answer = 0
    for key, value in dic.items():
        if value > 1:
            answer += value * (value - 1) // 2
        if (2 * key) in dic:
            answer += value * dic[(2 * key)]
        if int(1.5 * key) == 1.5 * key and int(1.5 * key) in dic:
            answer += value * dic[int(1.5 * key)]
        if int(4 / 3 * key) == 4 / 3 * key and int(4 / 3 * key) in dic:
            answer += value * dic[int(4 / 3 * key)]
    return answer
