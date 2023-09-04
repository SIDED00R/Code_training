def solution(myString):
    string = myString.split("x")
    return [len(num) for num in string]