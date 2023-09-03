def solution(myString):
    answer = ""
    for alp in myString:
        if ord(alp) < ord('l'):
            answer += "l"
        else:
            answer += alp
    return answer