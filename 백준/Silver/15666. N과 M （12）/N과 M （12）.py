import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

N, M = map(int, input().rstrip('\n').split())
line = list(map(int, input().rstrip('\n').split()))
line = sorted(line)
cases = combinations_with_replacement(line, M)
answer = set()
for case in cases:
    answer.add(case)

answer = sorted(answer)
for ans in answer:
    for num in ans:
        print(num, end = " ")
    print()
