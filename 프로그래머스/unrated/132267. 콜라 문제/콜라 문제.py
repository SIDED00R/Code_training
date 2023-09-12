def solution(a, b, n):
    answer = 0
    while n > a - 1:
        r = n % a
        get = (n // a) * b
        answer += get
        n = get + r
    return answer