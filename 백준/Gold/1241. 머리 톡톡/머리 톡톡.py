from collections import defaultdict

n = int(input())
dic = defaultdict(int)
answer = []
for _ in range(n):
    num = int(input())
    dic[num] += 1
    answer.append(num)

keep = [0 for _ in range(1000001)]
for i in range(1, 1000001):
    keep[i] += max(dic[i] - 1, 0)
    for idx in range(i * 2, 1000001, i):
        keep[idx] += dic[i]

for now in answer:
    print(keep[now])
        