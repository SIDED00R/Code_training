def countdevisor(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 2
    if int(n ** 0.5) ** 2 == n:
        count -= 1
    return count

def solution(number, limit, power):
    answer = 0
    for num in range(1, number + 1):
        n = countdevisor(num)
        if n > limit:
            answer += power
        else:
            answer += n
    return answer