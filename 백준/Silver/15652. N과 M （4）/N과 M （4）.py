import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

N, M = map(int, input().rstrip('\n').split())
cases = combinations_with_replacement(range(1, N + 1), M)
for case in cases:
    for num in case:
        print(num, end = " ")
    print()
