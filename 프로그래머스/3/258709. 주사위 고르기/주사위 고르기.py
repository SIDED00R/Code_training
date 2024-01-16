from itertools import combinations, product
from collections import defaultdict
import heapq

def make_heap(cases):
    dic = defaultdict(int)
    for case in cases:
        total = sum(case)
        dic[total] += 1
    heap = []
    for key, value in dic.items():
        heapq.heappush(heap, [key, value])
    return heap

def solution(dice):
    n = len(dice)
    dice_cases = list(combinations(range(n), n // 2))
    my_case = []
    your_case = []
    answer = []
    max_win = 0
    for dice_case in dice_cases:
        now_my_case = []
        now_your_case = []
        for idx in range(n):
            if idx in dice_case:
                now_my_case.append(dice[idx])
            else:
                now_your_case.append(dice[idx])
        my_case.append(now_my_case)
        your_case.append(now_your_case)
    
    for i in range(len(my_case)):
        my = my_case[i]
        you = your_case[i]
        my_diceroll_case = list(product(*my))
        you_diceroll_case = list(product(*you))
        my_heap = make_heap(my_diceroll_case)
        you_heap = make_heap(you_diceroll_case)
        win_total = 0
        you_less = 0
        while my_heap:
            while you_heap:
                if my_heap[0][0] > you_heap[0][0]:
                    you_dice = heapq.heappop(you_heap)
                    you_less += you_dice[1]
                else:
                    break
            my_dice = heapq.heappop(my_heap)
            win_total += you_less * my_dice[1]
            
        
        if max_win < win_total:
            max_win = win_total
            answer = dice_cases[i]
        
    return [i + 1 for i in answer]