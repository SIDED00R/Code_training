from bisect import bisect_left, bisect_right
from collections import defaultdict

def solution(words, queries):
    fwd, bwd = defaultdict(list), defaultdict(list)
    for w in words:
        fwd[len(w)].append(w)
        bwd[len(w)].append(w[::-1])
    for d in (fwd, bwd):
        for lst in d.values():
            lst.sort()

    answer = []
    for q in queries:
        n = len(q)
        if q[0] != '?':
            lst, key = fwd[n], q
        else:
            lst, key = bwd[n], q[::-1]
        lo, hi = key.replace('?', 'a'), key.replace('?', 'z')
        answer.append(bisect_right(lst, hi) - bisect_left(lst, lo))
    return answer