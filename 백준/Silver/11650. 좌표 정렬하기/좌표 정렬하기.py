n = int(input())
nlist = []
for _ in range(n):
    x, y = map(int, input().split())
    nlist.append([x, y])
nlist = sorted(nlist, key = lambda x : (x[0], x[1]))
for i in range(n):
    print(nlist[i][0], nlist[i][1])