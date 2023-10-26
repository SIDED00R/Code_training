def solution(topping):
    answer = 0
    dic = {}
    s = set()
    for num in topping:
        num = str(num)
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    
    total = len(dic)
    for num in topping:
        s.add(num)
        if dic[str(num)] == 1:
            total -= 1
        else:
            dic[str(num)] -= 1
        
        if total == len(s):
            answer += 1
        
    return answer