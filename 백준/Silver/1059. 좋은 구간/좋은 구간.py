import bisect

l = int(input())
line = sorted(list(map(int, input().split())))
line = [0] + line
n = int(input())
idx = bisect.bisect_right(line, n)
start = line[idx - 1]
end = line[idx]

if start == n:
    print(0)
else:
    front_diff = n - start
    back_diff = end - n
    print(front_diff * back_diff - 1)