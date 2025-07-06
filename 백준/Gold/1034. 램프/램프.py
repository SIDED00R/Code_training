from collections import defaultdict

n, m = map(int, input().split())
dic = defaultdict(int)
for _ in range(n):
    dic[input()] += 1
k = int(input())

l = []
for key, v in dic.items():
    l.append([v, key])
sort_l = sorted(l)

answer = 0
while sort_l:
    num, sim = sort_l.pop()
    zero_count = 0
    for now in sim:
        if now == '0':
            zero_count += 1
    if k >= zero_count and (k - zero_count) % 2 == 0:
        answer = num
        break

print(answer)