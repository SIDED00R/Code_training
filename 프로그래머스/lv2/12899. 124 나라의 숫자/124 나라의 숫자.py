def solution(n):
    num = []
    able = ["", "1", "2", "4"]
    while n != 0:
        r = n % 3
        n = n // 3
        num.append(r)
    for idx in range(len(num) - 1):
        if num[idx] <= 0:
            num[idx] += 3
            num[idx + 1] -= 1
    answer = ""
    for i in num[::-1]:
        answer += able[i]
    return answer