def solution(A,B):
    first = sorted(A)
    second = sorted(B, reverse = True)
    
    answer = 0
    for i in range(len(A)):
        answer += first[i] * second[i]

    return answer