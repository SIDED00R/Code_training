import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().rstrip('\n').split())
line = list(map(int, input().rstrip('\n').split()))
line.sort()
cases = permutations(line, M)
for case in cases:
    for num in case:
        print(num, end = " ")
    print()
