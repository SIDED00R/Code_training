def solution(N, number):
    total_case = [-1] * 32001
    total_case[0] = 0
    total_case[N] = 1
    able = [[], [N]]
    now = 1
    for now_idx in range(7):
        now += 1
        
        able_case = []
        first, second = 1, now - 1
        while first <= second:
            able_case.append([first, second])
            first += 1
            second -= 1
            now_able = []
        
        for f, s in able_case:
            first_case = able[f]
            second_case = able[s]
            for first_num in first_case:
                for second_num in second_case:
                    if first_num + second_num <= 32000 and total_case[first_num + second_num] == -1:
                        total_case[first_num + second_num] = now
                        now_able.append(first_num + second_num)
                    if first_num - second_num > 0 and total_case[first_num - second_num] == -1:
                        total_case[first_num - second_num] = now
                        now_able.append(first_num - second_num)
                    if second_num - first_num > 0 and total_case[second_num - first_num] == -1:
                        total_case[second_num - first_num] = now
                        now_able.append(second_num - first_num)
                    if second_num * first_num <= 32000 and total_case[second_num * first_num] == -1:
                        total_case[second_num * first_num] = now
                        now_able.append(second_num * first_num)
                    if total_case[int(first_num // second_num)] == -1:
                        total_case[int(first_num // second_num)] = now
                        now_able.append(int(first_num // second_num))
                    if total_case[int(second_num // first_num)] == -1:
                        total_case[int(second_num // first_num)] = now
                        now_able.append(int(second_num // first_num))
        special = N
        for _ in range(now - 1):
            special = special * 10 + N
        if special <= 32000:
            now_able.append(special)
            total_case[special] = now
        able.append(now_able)
    
    return total_case[number]

