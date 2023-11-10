def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    for i in range(len(A)):
        a = A[-1]
        b = B[-1]
        if b > a:
            answer += 1
            A.pop()
            B.pop()
        else:
            A.pop()
            
    return answer