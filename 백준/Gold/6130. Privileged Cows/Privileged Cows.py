n = int(input())
line = []
for _ in range(n):
    line.append(int(input()))

sort_line = sorted(line)

dic = {(1, 2):0, (1, 3):0, (2, 1):0, (2, 3):0, (3, 1):0, (3, 2):0, }
for idx in range(n):
    l = line[idx]
    s = sort_line[idx]
    if l != s:
        dic[(l, s)] += 1

answer = 0
ot = min(dic[(1, 2)], dic[(2, 1)])
tt = min(dic[(3, 2)], dic[(2, 3)])
to = min(dic[(1, 3)], dic[(3, 1)])
total = 0
for k, v in dic.items():
    total += v

left = total - 2 * (ot + tt + to)
answer = left + ot + tt + to - left // 3
print(answer)