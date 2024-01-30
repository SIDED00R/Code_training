import sys
from timeit import repeat
input = sys.stdin.readline
from itertools import combinations_with_replacement

N, M = map(int, input().rstrip('\n').split())
line = list(map(int, input().rstrip('\n').split()))
line.sort()
cases = combinations_with_replacement(line, M)
for case in cases:
    for num in case:
        print(num, end = " ")
    print()
