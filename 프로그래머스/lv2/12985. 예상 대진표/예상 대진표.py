def solution(n,a,b):
    find = False
    
    if a > b:
        a, b = b, a
        
    n //= 2
    criterion = n
    
    while not find:
        if a <= criterion < b:
            find = True
        elif b <= criterion:
            n //= 2
            criterion -= n
        elif a > criterion:
            n //= 2
            criterion += n
    
    answer = 0
    while n != 1:
        answer += 1
        n //= 2
    return answer + 1