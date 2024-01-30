import sys
from timeit import repeat
input = sys.stdin.readline
from itertools import product

N, M = map(int, input().rstrip('\n').split())
line = list(map(int, input().rstrip('\n').split()))
line.sort()
cases = product(line, repeat = M)
for case in cases:
    for num in case:
        print(num, end = " ")
    print()
