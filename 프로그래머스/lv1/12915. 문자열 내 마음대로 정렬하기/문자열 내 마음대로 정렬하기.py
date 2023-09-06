def solution(strings, n):
    string = sorted(strings)
    string = sorted(string, key = lambda x: x[n])
    return string