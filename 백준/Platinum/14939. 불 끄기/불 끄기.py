import copy
import sys
input = sys.stdin.readline
from itertools import product

def check(bulb, first_line):
    answer = 0
    dic = {"#":0, "O":1}
    simbol = ["O", "#"]
    
    # first line
    for idx ,num in enumerate(first_line):
        if num == 0:
            continue
        else:
            answer += 1
            bulb[0][idx] = simbol[dic[bulb[0][idx]]]
            bulb[1][idx] = simbol[dic[bulb[1][idx]]]
            if idx >= 1:
                bulb[0][idx - 1] = simbol[dic[bulb[0][idx - 1]]]
            if idx < 9:
                bulb[0][idx + 1] = simbol[dic[bulb[0][idx + 1]]]
    # middle line
    for i in range(9):
        for j in range(10):
            if bulb[i][j] == "O":
                answer += 1
                bulb[i][j] = simbol[dic[bulb[i][j]]]
                bulb[i + 1][j] = simbol[dic[bulb[i + 1][j]]]
                if i < 8:
                    bulb[i + 2][j] = simbol[dic[bulb[i + 2][j]]]
                if j >= 1:
                    bulb[i + 1][j - 1] = simbol[dic[bulb[i + 1][j - 1]]]
                if j < 9:
                    bulb[i + 1][j + 1] = simbol[dic[bulb[i + 1][j + 1]]]
    # check possible
    for i in range(10):
        if bulb[9][i] == "O":
            return -1              
    return answer

first_line_case = product([1, 0], repeat = 10)
bulb = []
for _ in range(10):
    bulb.append(list(input())[:-1])

min_value = 101
for first_line in first_line_case:
    copy_bulb = copy.deepcopy(bulb)
    ans = check(copy_bulb, first_line[::-1])
    if ans != -1 and ans < min_value:
        min_value = ans
        
if min_value == 101:
    print(-1)
else:
    print(min_value)
