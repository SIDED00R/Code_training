def isprime(p):
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True
    


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if isprime(i):
            answer += 1 
    return answer