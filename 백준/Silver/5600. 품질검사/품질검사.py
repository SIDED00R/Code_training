a, b, c = map(int, input().split())
n = int(input())
f = []
dic = {i : 0 for i in range(1, a + b + c + 1)}
for _ in range(n):
    i, j, k, r = map(int, input().split())
    if r == 1:
        dic[i] = 1
        dic[j] = 1
        dic[k] = 1
    else:
        f.append([i, j, k])

for f_case in f:
    i, j, k = f_case
    if dic[i] + dic[j] + dic[k] == 2:
        if dic[i] == 0:
            dic[i] = -1
        elif dic[j] == 0:
            dic[j] = -1
        else:
            dic[k] = -1

for i in range(1, a + b + c + 1):
    if dic[i] == 1:
        print(1)
    elif dic[i] == -1:
        print(0)
    else:
        print(2)