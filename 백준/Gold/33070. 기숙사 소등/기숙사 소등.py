import sys
import bisect
input = sys.stdin.readline

n, a = map(int, input().split())
line = sorted(list(map(int, input().split())))
light = list(map(int, input().split()))

answer = 0
min_count = 0
max_count = 0
for idx in range(n):
    now_light = light[idx]
    if now_light == 1:
        left = bisect.bisect_left(line, min_count)
        right = bisect.bisect_right(line, max_count)
        if left < right:
            max_count += 1
    else:
        min_count += 1
        max_count += 1

print(n - max_count)
    