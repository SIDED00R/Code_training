from bisect import bisect_right
n = int(input())
line = sorted(map(int, input().split()))
q = int(input())
for _ in range(q):
    m = int(input())
    print(bisect_right(line, m))