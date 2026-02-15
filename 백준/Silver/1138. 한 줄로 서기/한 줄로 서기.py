from itertools import permutations

n = int(input())
line = list(map(int, input().split()))
for now_case in permutations(range(n)):
    find = True
    for i in range(n):
        count = 0
        for j in range(i):
            if now_case[i] < now_case[j]:
                count += 1
        if count != line[now_case[i]]:
            find = False
            break
    if find:
        for num in now_case:
            print(num + 1, end = " ")
        exit()