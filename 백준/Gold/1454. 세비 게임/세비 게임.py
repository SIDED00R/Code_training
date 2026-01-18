from itertools import combinations, product
from collections import defaultdict, Counter

def able(k, dice, dice_case):
    not_change = [i for i in range(5) if i not in k]
    find = True
    for idx in not_change:
        if dice[idx] != dice_case[idx]:
            find = False
            break
    return find

def sebi(dice_case):
    if dice_case[0] == dice_case[1] == dice_case[2] == dice_case[3] == dice_case[4]:
        return True
    return False

def sebistraight(dice_case):
    dice_case = sorted(dice_case)
    if dice_case == [1, 2, 3, 4, 5] or dice_case == [2, 3, 4, 5, 6]:
        return True
    return False

def straight(dice_case):
    dice_case = sorted(set(dice_case))
    if len(dice_case) == 4 and ((dice_case[0] + 3 == dice_case[1] + 2 == dice_case[2] + 1 == dice_case[3])):
        return True
    elif len(dice_case) == 5 and((dice_case[0] + 3 == dice_case[1] + 2 == dice_case[2] + 1 == dice_case[3]) or (dice_case[1] + 3 == dice_case[2] + 2 == dice_case[3] + 1 == dice_case[4])):
        return True
    return False

def full(dice_case):
    c = Counter(dice_case)
    vals = sorted(c.values())
    return vals == [5] or vals == [2, 3] 
   
dic = {}
for i in range(2, 6):
    for now_case in sorted(combinations(range(5), i)):
        dic[now_case] = 0

score = list(map(int, input().split()))
dice = list(map(int, input().split()))

for dice_case in product(range(1, 7), repeat = 5):
    for k, _ in dic.items():
        if able(k, dice, dice_case):
            now_score = 0
            if sebi(dice_case):
                now_score = max(now_score, score[0])
            if sebistraight(dice_case):
                now_score = max(now_score, score[1])
            if straight(dice_case):
                now_score = max(now_score, score[2])
            if full(dice_case):
                now_score = max(now_score, score[3])
            dic[k] += now_score

min_value = 1e20
for k, v in dic.items():
    length = len(k)
    exp = v / (6 ** length)
    if exp < min_value or (exp == min_value and k < answer):
        min_value = exp
        answer = k

print(len(answer))
for num in answer:
    print(num + 1, end = " ")
        
