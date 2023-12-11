def solution(scores):
    N = len(scores)
    able_num = [0] * (100001)
    dic = {}
    for score in scores:
        first, second = score
        if first in dic:
            if dic[first] < second:
                dic[first] = second
        else:
            dic[first] = second
    for key, value in dic.items():
        able_num[key] = value
    
    max_value = 0
    for i in range(100000, -1, -1):
        if able_num[i] > max_value:
            max_value = able_num[i]
        else:
            able_num[i] = max_value
            
    for idx, case in enumerate(scores):
        if case[0] != 100000:
            if able_num[case[0] + 1] > case[1]:
                scores[idx] = -1
            else:
                scores[idx] = case[0] + case[1]
        else:
            scores[idx] = case[0] + case[1]
    
    wanho = scores[0]
    
    if wanho == -1:
        return -1
    else:
        answer = 1
        for num in scores:
            if num > wanho:
                answer += 1
            
    return answer