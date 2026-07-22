import random

def check(line, simbol, num):
    next_case = []
    for now_case in line:
        s = b = 0
        for idx in range(4):
            now_num = now_case[idx]
            if now_num == num[idx]:
                s += 1
            elif now_num in num:
                b += 1
        if [s, b] == simbol:
            next_case.append(now_case)
    return next_case

def solution(n, submit):
    line = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    if len({i, j, k, l}) == 4:
                        line.append(f"{i}{j}{k}{l}")
    count = 0
    while True:
        count += 1
        if count == 1:
            now_case = "1234"
        else:
            now_case = line[0]
        s = submit(int(now_case))
        if s == "4S 0B":
            return int(now_case)
        else:
            line = check(line, [int(s[0]), int(s[3])], now_case)
        if len(line) == 1:
            return int(line[0])