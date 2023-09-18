import sys
n = int(input())
for _ in range(n):
    N, idx = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))

    sortimport = sorted(importance)
    find = False

    importance = [[importance[i],i] for i in range(N)]

    count = 0

    while find != True :
        count += 1
        maximport = sortimport.pop()
        for i in range(len(importance)):
            if importance[i][0] == maximport:
                if importance[i][1] == idx:
                    print(count)
                    find = True
                importance = importance[i + 1:] + importance[:i]
                break

