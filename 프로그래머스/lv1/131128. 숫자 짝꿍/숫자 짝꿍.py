def solution(X, Y):
    answer = ""
    X = [i for i in X]
    Y = [i for i in Y]
    num = [min(X.count(str(i)), Y.count(str(i))) for i in range(10)]
    for n in range(9, -1, -1):
        answer = answer + (num[n] * str(n))
    if answer == "":
        return "-1"
    elif answer[0] == "0":
        return "0"
    return answer