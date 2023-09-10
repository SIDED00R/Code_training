def solution(lottos, win_nums):
    correct = 0
    possible = 0
    for num in lottos:
        if num in win_nums:
            correct += 1
        elif num == 0:
            possible += 1
    
    return [min(6, 7 - possible - correct), min(6, 7 - correct)]