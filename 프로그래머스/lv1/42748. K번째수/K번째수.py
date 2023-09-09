def solution(array, commands):
    answer = []
    for i in commands:
        l = array[i[0] - 1:i[1]]
        l = sorted(l)
        answer.append(l[i[2] - 1])
        
    return answer