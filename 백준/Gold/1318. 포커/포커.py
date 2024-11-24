a = [0, 6612900, 9730740, 2532816, 732160, 282060, 39780, 39780, 205976, 165984, 14664, 1472, 188]

import math
from itertools import combinations
from fractions import Fraction

answer = [0] * 13

total = math.comb(52, 6)


for ans_num in a[1:]:
    print(Fraction(ans_num, total))
exit()

def count_number(card_list):
    max_num = 0
    second_max = 0
    for num in set(card_list):
        now_count = 0
        for i in range(6):
            if card_list[i] == num:
                now_count += 1
        if max_num <= now_count:
            second_max = max_num
            max_num = now_count
        elif second_max < now_count:
            second_max = now_count
    return (max_num, second_max)

def is_st(card_list):
    unique_numbers = sorted(set(card_list))
    length = len(unique_numbers)
    if length == 5:
        if unique_numbers[0] + 4 == unique_numbers[4]:
            return True
    elif length == 6:
        if unique_numbers[0] + 4 == unique_numbers[4] or unique_numbers[1] + 4 == unique_numbers[5]:
            return True
    return False

for now in combinations(range(52), 6):
    shape = []
    number = []
    
    for num in now:
        shape.append(num // 13)
        number.append(num % 13)

    first_count, second_count = count_number(number)
    sorted_number = sorted(number)

    if (shape[0] == shape[4] and number[0] == 0 and number[4] == 4) or (shape[1] == shape[5] and number[1] == 0 and number[5] == 4):
        answer[12] += 1
    elif (shape[0] == shape[4] and number[0] + 4 == number[4]) or (shape[1] == shape[5] and number[1] + 4 ==number[5]):
        answer[11] += 1
    elif first_count == 4:
        answer[10] += 1
    elif first_count == 3 and second_count >= 2:
        answer[9] += 1
    elif shape[0] == shape[4] or shape[1] == shape[5]:
        answer[8] += 1
    elif 0 in number and 9 in number and 10 in number and 11 in number and 12 in number:
        answer[7] += 1
    elif 0 in number and 1 in number and 2 in number and 3 in number and 4 in number:
        answer[6] += 1
    elif is_st(number):
        answer[5] += 1
    elif first_count == 3:
        answer[4] += 1
    elif first_count == 2 and second_count == 2:
        answer[3] += 1
    elif first_count == 2:
        answer[2] += 1
    else:
        answer[1] += 1

for ans_num in answer[1:]:
    print(Fraction(ans_num, total))
