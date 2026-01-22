from bisect import bisect_right
import sys
input = sys.stdin.readline

def find(a, b, c ,j):
    front = 0
    back = int(1e10)
    while front < back:
        mid = (front + back) // 2
        alpha = bisect_right(l[a - 1], mid)
        beta = bisect_right(l[b - 1], mid)
        gamma = bisect_right(l[c - 1], mid)
        if alpha + beta + gamma >= j:
            back = mid
        else:
            front = mid + 1
    return back
    
n, q = map(int, input().split())
l = []
for _ in range(n):
    l.append(sorted(list(map(int, input().split()))[1:]))

for _ in range(q):
    a, b, c, j = map(int, input().split())
    print(find(a, b, c, j))