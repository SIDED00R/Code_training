def solution(strings, n):
    string = sorted(strings, key = lambda x: [x[n], x])
    return string