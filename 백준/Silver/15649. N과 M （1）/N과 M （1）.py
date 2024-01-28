import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().rstrip('\n').split())
cases = permutations(range(1, N + 1), M)
for case in cases:
    for num in case:
        print(num, end = " ")
    print()
