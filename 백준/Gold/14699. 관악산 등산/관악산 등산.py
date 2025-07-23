from collections import defaultdict

n, m = map(int, input().split())
height = list(map(int, input().split()))
sort_height = []
for idx, num in enumerate(height):
    sort_height.append([num, idx + 1])
sort_height = sorted(sort_height)

dic = defaultdict(list)
for _ in range(m):
    s, e = map(int, input().split())
    sh = height[s - 1]
    eh = height[e - 1]
    if sh > eh:
        dic[s].append(e)
    else:
        dic[e].append(s)

answer = [0] * (n + 1)
while sort_height:
    num, idx = sort_height.pop()
    if answer[idx] == 0:
        answer[idx] = 1
    for able_case in dic[idx]:
        answer[able_case] = max(answer[able_case], answer[idx] + 1)

for num in answer[1:]:
    print(num)
        