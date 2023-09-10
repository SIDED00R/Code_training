def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if int(num ** 0.5) ** 2 == num:
            answer -= num
        else:
            answer += num
    return answer