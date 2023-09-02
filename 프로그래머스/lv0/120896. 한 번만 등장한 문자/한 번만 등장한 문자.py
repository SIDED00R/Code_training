def solution(s):
    answer = list(s)
    answer.sort()
    remove = ""
    for idx in range(1,len(answer)):
        if answer[idx] == answer[idx - 1]:
            remove += answer[idx]
    answer = "".join(answer)
    for alp in remove:
        answer = answer.replace(alp,"")
    
    return answer