from collections import Counter
import math
t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    new_list = [line[i] - i for i in range(n)]
    dic = Counter(new_list)
    answer = 0
    for k, v in dic.items():
        if v == 1:
            continue
        answer += math.comb(v, 2)
    print(answer)