def solution(s):
    
    start = ""
    a, b = 1, 0
    answer = 0
    
    for alp in s:
        if start == "":
            start = alp
        else:
            if start == alp:
                a += 1
            else:
                b += 1
        if a == b:
            start = ""
            a, b = 1, 0
            answer += 1
            
    return answer + (start != "") 