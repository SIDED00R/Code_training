def solution(numlist, n):
    answer = []
    n1 = n
    n2 = n
    if n in numlist:
        answer = [n]
    while len(answer) != len(numlist):
        n1 += 1
        n2 -= 1
        if n1 in numlist:
            answer.append(n1)
        if n2 in numlist:
            answer.append(n2)
    return answer