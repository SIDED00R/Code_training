import sys
input = sys.stdin.readline

N = int(input())
G = []
link_nodes = [[] for _ in range(N)]
for i in range(N):
    line = list(input().rstrip('\n').split())
    for j in range(N):
        if line[j] == "1":
            link_nodes[i].append(j)
    G.append(line)
    
for i in range(N):
    stack = link_nodes[i][:]
    while stack:
        num = stack.pop()
        for case in link_nodes[num]:
            if G[i][case] == "0":
                G[i][case] = "1"
                stack.append(case)
for row in G:
    print(" ".join(row))