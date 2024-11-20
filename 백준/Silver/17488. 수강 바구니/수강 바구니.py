from collections import defaultdict

dic = defaultdict(list)
n, m = map(int, input().split())
line = [0] + list(map(int, input().split()))
answer = [[] for _ in range(n + 1)]
for i in range(n):
    now = list(map(int, input().split()))
    for num in now:
        if num != -1:
            dic[num].append(i + 1)
            line[num] -= 1

for idx in range(1, m + 1):
    if line[idx] >= 0:
        for num in dic[idx]:
            answer[num].append(idx)

dic = defaultdict(list)
for i in range(n):
    now = list(map(int, input().split()))
    for num in now:
        if num != -1:
            dic[num].append(i + 1)
            line[num] -= 1

for idx in range(1, m + 1):
    if line[idx] >= 0:
        for num in dic[idx]:
            answer[num].append(idx)

for ans in answer[1:]:
    if ans == []:
        print("망했어요")
    else:
        ans = sorted(ans)
        for num in ans:
            print(num, end = " ")
        print()
