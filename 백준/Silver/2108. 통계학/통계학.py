import sys

n = int(input())

num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num = sorted(num)

dic = {}
for i in num:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

most = max(dic.values())

countmost = []
for i in dic:
    if most == dic[i]:
        countmost.append(i)

print(round(sum(num) / n))
print(num[n//2])

if len(countmost) > 1:
    print(countmost[1])
else:
    print(countmost[0])
print(num[-1] - num[0])

