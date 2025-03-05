from itertools import permutations

cow = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
n = int(input())
next_cow_list = []
for _ in range(n):
    line = list(input().split())
    next_cow_list.append([line[0], line[-1]])


answer = []
for now in permutations(range(8), 8):
    dic = {cow[idx]:now[idx] for idx in range(8)}
    find = True
    for next_cow in next_cow_list:
        if abs(dic[next_cow[0]] - dic[next_cow[1]]) == 1:
            continue
        else:
            find = False
            break
    if find:
        ans = ["" for _ in range(8)]
        for idx in range(8):
            ans[now[idx]] = cow[idx]
        answer.append(ans)

for a in (sorted(answer)[0]):
    print(a)