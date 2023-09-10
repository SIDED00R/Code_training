def solution(n):
    tnum = []
    while n != 0:
        tnum.append(n % 3)
        n //= 3
    t = 1
    answer = 0
    for num in tnum[::-1]:
        answer += t*num
        t *= 3
    return answer