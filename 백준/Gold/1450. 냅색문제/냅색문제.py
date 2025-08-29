import sys
from bisect import bisect_right
input = sys.stdin.readline

def gen_subset_sums(arr):
    sums = [0]
    for x in arr:
        sums += [s + x for s in sums]
    return sums

N, C = map(int, input().split())
weights = list(map(int, input().split()))
left = weights[:N//2]
right = weights[N//2:]
L = gen_subset_sums(left)
R = gen_subset_sums(right)
L = [s for s in L if s <= C]
R = [s for s in R if s <= C]
R.sort()
ans = 0
for s in L:
    ans += bisect_right(R, C - s)
print(ans)