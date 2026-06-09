import sys
from collections import defaultdict
input = sys.stdin.readline

def get_path(num):
    path = {}
    ops = 0
    seen = set()
    while num not in seen:
        seen.add(num)
        path[num] = ops
        if num % 2 == 0:
            num //= 2
        else:
            num += 1
        ops += 1
    return path

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    paths = [get_path(num) for num in a]
    
    common = set(paths[0].keys())
    for p in paths[1:]:
        common &= set(p.keys())
    
    ans = min(sum(p[v] for p in paths) for v in common)
    print(ans)
