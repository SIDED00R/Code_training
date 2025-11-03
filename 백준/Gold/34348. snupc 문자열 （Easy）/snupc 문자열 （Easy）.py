from collections import defaultdict
from bisect import bisect_right, bisect_left

line = input()

dic = defaultdict(list)

for idx in range(len(line)):
    alp = line[idx]
    dic[alp].append(idx)

n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    L = l - 1
    R = r - 1
    start = 1
    end = (r - l + 1) // 5
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        now_idx = L - 1
        ok = True
        for now_case in ['s', 'n', 'u', 'p', 'c']:
            idx = bisect_left(dic[now_case], now_idx + 1)
            j = idx + mid - 1
            if j >= len(dic[now_case]) or dic[now_case][j] > R:
                ok = False
                break
            now_idx = dic[now_case][j]
        if ok:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)