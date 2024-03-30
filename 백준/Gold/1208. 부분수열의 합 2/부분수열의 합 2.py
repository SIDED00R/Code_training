import sys
input = sys.stdin.readline
from itertools import combinations
from collections import defaultdict

def find_subseq(arr):
    answer = []
    for i in range(1, len(arr) + 1):
        answer += list(combinations(arr, i))
    return answer

def sum_subseq(arr):
    answer = defaultdict(int)
    for case in arr:
        answer[sum(case)] += 1
    return answer


N, S = map(int, input().split())
middle = N // 2
line = list(map(int, input().split()))
front = line[:middle]
back = line[middle:]

first_case = sum_subseq(find_subseq(front))
second_case = sum_subseq(find_subseq(back))

answer = 0
for key, value in first_case.items():
    if key == S:
        answer += value
    if S - key in second_case:
        answer += value * second_case[S - key]
for key, value in second_case.items():
    if key == S:
        answer += value
        
print(answer)

