import sys
input = sys.stdin.readline
from itertools import combinations

def different(first, second):
    diff = 0
    for i in range(4):
        if first[i] != second[i]:
            diff += 1
    return diff        
    
T = int(input())
for _ in range(T):
    answer = 12
    N = int(input())
    cases = input().rstrip('\n').split()
    if N > 32:
        print(0)
        continue
    for case in list(combinations(cases, 3)):
        now = 0
        for i in range(3):
            now += different(case[i], case[(i + 1) % 3])
        if answer > now:
            answer = now
    print(answer)        