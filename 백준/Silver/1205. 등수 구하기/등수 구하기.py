from bisect import bisect_right

n, score, p = map(int, input().split())

if n == 0:
    print(1)
    exit()

score_list = list(map(int, input().split()))

if n == p and score <= score_list[-1]:
    print(-1)
else:
    asc = score_list[::-1]
    rank = n - bisect_right(asc, score) + 1
    print(rank)