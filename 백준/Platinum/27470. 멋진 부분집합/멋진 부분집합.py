import random
import sys
import math
input = sys.stdin.readline

def prime_factors_distinct(x: int):
    ret = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            ret.append(d)
            while x % d == 0:
                x //= d
        d += 1 if d == 2 else 2  
    if x > 1:  
        ret.append(x)
    return ret

n = int(input())
line = list(map(int, input().split()))
target = (n + 1) // 2

tries = min(40, n)
indices = random.sample(range(n), tries)

checked = set()
final_answer = None

for idx in indices:
    x = line[idx]
    for p in prime_factors_distinct(x):
        if p in checked:
            continue
        checked.add(p)

        ans = []
        for v in line:
            if v % p == 0:
                ans.append(v)
                if len(ans) == target:
                    final_answer = ans
                    break
        if final_answer is not None:
            break
    if final_answer is not None:
        break

if final_answer is not None:
    print("YES")
    print(*final_answer)
else:
    print("NO")