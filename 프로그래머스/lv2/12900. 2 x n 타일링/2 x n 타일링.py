def solution(n):
    a = 1
    b = 1
    if n == 2:
        return 2
    else:
        for i in range(n):
            a, b = b, a + b
        
    return a % 1000000007