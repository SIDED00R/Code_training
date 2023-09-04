def solution(A, B):
    for i in range(len(A)):
        if A == B:
            return i
        B = B[1:] + B[0]
    return -1