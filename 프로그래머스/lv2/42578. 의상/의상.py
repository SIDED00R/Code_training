def solution(clothes):
    dic = {}
    answer = 1
    for clothe, case in clothes:
        if case not in dic:
            dic[case] = [clothe]
        else:
            dic[case] += [clothe]
    
    for num in dic.values():
        answer *= len(num) + 1
    
    return answer - 1