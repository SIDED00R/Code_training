from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = defaultdict(int)
cnt[0] = 1

s = 0
ans = 0
for x in arr:
    s += x
    ans += cnt[s - k]
    cnt[s] += 1

print(ans)