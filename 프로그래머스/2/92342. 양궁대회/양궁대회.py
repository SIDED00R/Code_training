from itertools import product

def solution(n, info):
    max_gap = 1
    answer = []
    for case in product(("O", "X"), repeat = 11):
        my_shoot = 0
        for i in range(11):
            if case[i] == "O":
                my_shoot += info[i] + 1
                
        if my_shoot <= n:
            my_score = 0
            your_score = 0
            for j in range(11):
                if case[j] == "O":
                    my_score += 10 - j
                elif case[j] != "O" and info[j] != 0:
                    your_score += 10 - j
            
            same = False
            if my_score - your_score >= max_gap:
                if my_score - your_score == max_gap:
                    same = True
                max_gap = my_score - your_score
                able = []
                for k in range(11):
                    if case[k] == "O":
                        able.append(info[k] + 1)
                    else:
                        able.append(0)
                able[-1] += n - my_shoot
                
                if not same:
                    answer = able
                else:
                    for k in range(10, -1, -1):
                        if able[k] > answer[k]:
                            answer = able
                            
                            break
                        elif able[k] == answer[k]:
                            continue
                        else:
                            break
                        

    if answer == []:
        return [-1]
    else:
        return answer

