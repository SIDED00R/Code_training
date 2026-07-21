from collections import defaultdict
from itertools import product

def solution(hints, costs):
    answer = 1e20
    for now_case in product([0, 1], repeat = len(costs)):
        now_answer = 0
        now_dic = defaultdict(int)
        for idx, able in enumerate(now_case):
            if able:
                now_answer += costs[idx][0]
                for hint_idx in costs[idx][1:]:
                    now_dic[hint_idx] += 1
        for idx in range(len(hints)):
            now_hint_count = min(len(costs), now_dic[idx + 1])
            now_answer += hints[idx][now_hint_count]
        answer = min(answer, now_answer)
    return answer
