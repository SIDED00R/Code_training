from collections import defaultdict

dic = defaultdict(int)
n = int(input())
word = input()
for alp in word:
    if alp in "HIARC":
        dic[alp] += 1

answer = n
for key in "HIARC":
    value = dic[key]
    answer = min(answer, value)

print(answer)