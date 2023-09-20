def largedivisor(num):
    if num > 10000000:
        able = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                able.append(i)
                if num // i < 10000001:
                    able.append(num // i)
        return max(able)
    else:
        for i in range(num - 1, int(num**0.5) - 1, -1):
            if num % i == 0:
                return i
    return 1


def solution(begin, end):
    answer = []
    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
        else:
            answer.append(largedivisor(num))
        
    return answer