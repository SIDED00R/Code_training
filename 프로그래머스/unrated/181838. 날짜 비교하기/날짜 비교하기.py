def solution(date1, date2):
    for idx, num in enumerate(date1):
        if num < date2[idx]:
            return 1
        elif num > date2[idx]:
            return 0
    return 0