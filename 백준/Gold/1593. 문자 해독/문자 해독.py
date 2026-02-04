from collections import defaultdict
import sys
input = sys.stdin.readline

w, g = map(int, input().split())
word = list(input().rstrip('\n'))
s = list(input())

answer_dic = defaultdict(int)
for alp in word:
    answer_dic[alp] += 1

stack_dic = defaultdict(int)
answer = 0
for idx in range(w):
    stack_dic[s[idx]] += 1
if answer_dic == stack_dic:
    answer += 1
for idx in range(w, g):
    stack_dic[s[idx - w]] -= 1
    if stack_dic[s[idx - w]] == 0:
        del stack_dic[s[idx - w]]
    stack_dic[s[idx]] += 1
    if answer_dic == stack_dic:
        answer += 1

print(answer)
    