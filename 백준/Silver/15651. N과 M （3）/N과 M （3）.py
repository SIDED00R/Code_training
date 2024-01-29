import sys
input = sys.stdin.readline
from itertools import product

N, M = map(int, input().rstrip('\n').split())
cases = product(range(1, N + 1), repeat = M)
for case in cases:
    for num in case:
        print(num, end = " ")
    print()
