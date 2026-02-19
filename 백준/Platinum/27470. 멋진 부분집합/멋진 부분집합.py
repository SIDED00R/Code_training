import random
import sys
import math
input = sys.stdin.readline

def check(x):
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
target = math.ceil(n / 2)
result = random.sample(range(0, n), min(40, n))

line = list(map(int, input().split()))
find = False
p_dic = {}
for idx in result:
    num = line[idx]
    l = check(num)
    for p in l:
        if find:
            break
        if p in p_dic:
            continue
        else:
            p_dic[p] = 0
            answer = []
            count = 0
            for now_num in line:
                if now_num % p == 0:
                    count += 1
                    answer.append(now_num)
                    if count == target:
                        find = True
                        break
if find:
    print("YES")
    print(*answer)
else:
    print("NO")