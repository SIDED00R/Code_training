def solution(s):
    first = True
    answer = ""
    for alp in s:
        
        if alp == " ":
            answer += alp
            first = True 
        elif first:
            answer += alp.upper()
            first = False   
        else:
            answer += alp.lower()
    return answer
            