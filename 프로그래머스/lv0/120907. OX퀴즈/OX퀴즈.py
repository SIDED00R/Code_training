def solution(quiz):
    answer = []
    for q in quiz:
        e = q.split()
        if e[1] == "+":
            if int(e[0]) + int(e[2]) == int(e[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(e[0]) - int(e[2]) == int(e[4]):
                answer.append("O")
            else:
                answer.append("X")
        
    return answer