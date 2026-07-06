import math
from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    line = list(input())
    for idx in range(n):
        line[idx] = int(line[idx]) - 1

    p_sum = [0]
    for idx in range(n):
        p_sum.append(p_sum[-1] + line[idx])

    answer = 0
    for k, v in Counter(p_sum).items():
        if v >= 2:
            answer += math.comb(v, 2)
    print(answer)