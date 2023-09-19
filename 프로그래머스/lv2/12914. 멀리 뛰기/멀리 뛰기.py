def solution(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = a + b, a
    
    
    return b % 1234567