from itertools import combinations

def solution(n, q, ans):
    answer = 0
    for case in combinations(range(1, n + 1), 5):
        find = True
        for idx in range(len(q)):
            now_q = q[idx]
            now_ans = ans[idx]
            count = 0
            for i in range(5):
                if case[i] in now_q:
                    count += 1
            if count != now_ans:
                find = False
                break
        if find:
            answer += 1

    return answer