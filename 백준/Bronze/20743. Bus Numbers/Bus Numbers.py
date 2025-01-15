from collections import defaultdict

triple = []
for num in range(1, 74):
    triple.append(num ** 3)

dic = defaultdict(int)
for i in range(len(triple)):
    for j in range(i + 1, len(triple)):
        dic[triple[i] + triple[j]] += 1

answer = []
for k, v in dic.items():
    if v >= 2:
        answer.append(k)

answer.sort()

n = int(input())
ans = 0
for bus in answer:
    if bus <= n:
        ans = bus
    else:
        break

if ans == 0:
    print("none")
else:
    print(ans)
