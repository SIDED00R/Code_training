import sys

N, M = map(int, input().split())
d = {}
for i in range(N):
    site, id = sys.stdin.readline().split()
    d[site] = id

for i in range(M):
    site = input()
    print(d[site])


