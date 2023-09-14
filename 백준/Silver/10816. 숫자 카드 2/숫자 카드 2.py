import sys
a = input()
have = sys.stdin.readline().split()
dic = {}

for num in have:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

b = input()

how = sys.stdin.readline().split()

answer = []
for num in how:
    if num in dic:
        answer.append(dic[num])
    else:
        answer.append(0)
print(" ".join(map(str, answer)))