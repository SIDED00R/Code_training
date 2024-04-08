import sys
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())
word = sorted(list(input().split()))
for case in combinations(word, L):
    vowel_count = 0
    for vowel in ["a", "e", "i", "o", "u"]:
        if vowel in case:
            vowel_count += 1
    if vowel_count == 0 or len(case) - vowel_count < 2:
        continue
    else:
        print("".join(case))