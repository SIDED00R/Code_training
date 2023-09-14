def solution(name, yearning, photo):
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    answer = []
    for pic in photo:
        num = 0
        for people in pic:
            if people in dic:
                num += dic[people]
        answer.append(num)
    return answer