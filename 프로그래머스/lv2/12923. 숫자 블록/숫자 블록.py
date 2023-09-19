def largedivisor(num):
    if num == 1:
        return 0
    able = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and i <= 1e7:
            able.append(i)
            if num // i <= 1e7 and num // i != num:
                able.append(num // i)
        
    return max(able)

def solution(begin, end):
    answer = []
    for num in range(begin, end + 1):
        largenum = largedivisor(num)
        answer.append(largenum)
    return answer