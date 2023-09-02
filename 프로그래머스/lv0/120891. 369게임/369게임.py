def solution(order):
    answer = 0
    while order != 0:
        last_num = order % 10
        if last_num != 0 and last_num % 3 == 0:
            answer += 1
        order //= 10
    return answer