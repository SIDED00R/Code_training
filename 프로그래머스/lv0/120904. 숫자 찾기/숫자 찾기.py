def solution(num, k):
    count = 0
    find = 0
    while num != 0:
        count += 1
        if k == num % 10:
            find = count
        num //= 10
    if find == 0:
        return -1
               
    return count - find + 1