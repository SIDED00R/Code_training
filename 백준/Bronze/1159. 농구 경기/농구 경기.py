from collections import defaultdict

n = int(input())
dic = defaultdict(int)
for _ in range(n):
    name = input()
    dic[name[0]] += 1

answer = ""
for k in sorted(dic):
    if dic[k] >= 5:
        answer += k

if answer == "":
    print("PREDAJA")
else:
    print(answer)