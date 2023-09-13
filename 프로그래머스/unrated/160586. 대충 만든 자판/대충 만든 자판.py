def solution(keymap, targets):
    dic = {chr(65 + n) : 101 for n in range(26)}
    for key in keymap:
        count = 1
        for alp in key:
            dic[alp] = min(dic[alp], count)
            count += 1
    
    answer = []
    for target in targets:
        result = 0
        for alp in target:
            if dic[alp] == 101:
                result = -1
                break
            result += dic[alp]
        answer.append(result)
            
    return answer