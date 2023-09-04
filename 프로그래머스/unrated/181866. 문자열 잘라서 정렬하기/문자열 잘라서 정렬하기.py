def solution(myString):
    string = myString.split("x")
    answer = sorted(list(filter(None,string)))
    return answer