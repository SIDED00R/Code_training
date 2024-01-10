def solution(e, starts):
    table = [[] for _ in range(e + 1)]
    answer_table = [0] * (e + 1)
    answer_table[1] = 1
    answer_max_advent_idx = [0] * (e + 1)
    for i in range(2, e + 1):
        if not table[i]:
            for j in range(i, e + 1, i):
                table[j].append(i)
    for i in range(2, e + 1):
        now_idx = i
        total = 1
        for prime in table[i]:
            how_many = 0
            while i % prime == 0:
                how_many += 1
                i //= prime
            total *= (how_many + 1)
        answer_table[now_idx] = total
    
    max_advent = 0
    max_advent_idx = -1
    for idx in range(e, 0, -1):
        now_advent = answer_table[idx]
        if now_advent >= max_advent:
            max_advent = now_advent
            answer_max_advent_idx[idx] = idx
            max_advent_idx = idx
        else:
            answer_max_advent_idx[idx] = max_advent_idx
    
    answer = []
    for start in starts:
        answer.append(answer_max_advent_idx[start])
    return answer