def solution(dartResult):
    collect = []
    score = ""
    answer = 0
    check = False
    for i in dartResult:
        if i == "S":
            collect.append(int(score))
        elif i == "D":
            collect.append(int(score) ** 2)
        elif i == "T":
            collect.append(int(score) ** 3)
        elif i == "*":
            collect = [i * 2 for i in collect] 
            check = True
        elif i == "#":
            collect[-1] *= -1
            check = True
        else:   
            answer += sum(collect[:-1])
            collect = collect[-1:]
            score += i
            continue
        score = ""
        
    return answer + sum(collect)