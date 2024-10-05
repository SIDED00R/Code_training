from collections import defaultdict

r, c = map(int, input().split())
dic = defaultdict(list)
for _ in range(r):
    line = input()
    count = 0
    for case in line[:-1][::-1]:
        if case == ".":
            count += 1
        elif case == "S":
            continue
        else:
            dic[count].append(int(case))
            break


answer = [0] * 9
now = 1
for idx in range(c - 4):
    if idx in dic:
        for num in dic[idx]:
            answer[num - 1] = now
        now += 1

for num in answer:
    print(num)
