from collections import Counter
from bisect import bisect_left

def able(first, second, num):
    fs = str(first)
    ss = str(second)
    s = fs + ss
    ns = str(num)
    if len(ns) == len(s) and Counter(s) == Counter(ns):
        return True
    else:
        return False

def check(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if able(i, num // i, num):
                return True
    return False
            
l = []
for num in range(100, 1000256):
    if check(num):
        l.append(num)

while True:
    n = int(input())
    if n == 0:
        break
    print(l[bisect_left(l, n)])