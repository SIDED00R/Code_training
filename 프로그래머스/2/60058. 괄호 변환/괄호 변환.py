def solution(p):
    answer = ""

    if p =="":
        return ""

    u = v = ""

    count = 0

    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        u += p[i]
        if count == 0:
            v = p[i + 1:]
            break
    if u[0] == "(":
        return u + solution(v)

    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        for alp in u[1:-1]:
            if alp == "(":
                answer += ")"
            else:
                answer += "("
        return answer