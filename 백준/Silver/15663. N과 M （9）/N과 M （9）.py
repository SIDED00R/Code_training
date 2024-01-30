import sys
from timeit import repeat
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().rstrip('\n').split())
line = list(map(int, input().rstrip('\n').split()))

cases = permutations(line, M)
answer = set()
for case in cases:
    answer.add(case)

answer = sorted(answer)
for ans in answer:
    for num in ans:
        print(num, end = " ")
    print()
