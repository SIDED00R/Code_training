import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find_parents(parents, now):
    if parents[now] != now:
        parents[now] = find_parents(parents, parents[now])
    return parents[now]

def union(first, second, parents):
    second_parent = find_parents(parents, second)
    if first != second_parent:
        parents[first] = second_parent

G = int(input())
P = int(input())

count = 0
parents = [i for i in range(G + 1)]
for i in range(P):
    g_i = int(input())
    now_parent = find_parents(parents, g_i)
    if now_parent == 0:
        break
    union(now_parent, now_parent - 1, parents)
    count += 1
    
print(count)