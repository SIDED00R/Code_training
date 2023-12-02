def solution(n, money):
    total_case = [1] + [0] * n
    for cash in money:
        for num in range(cash, n + 1):
            total_case[num] += total_case[num - cash]
    return total_case[-1]