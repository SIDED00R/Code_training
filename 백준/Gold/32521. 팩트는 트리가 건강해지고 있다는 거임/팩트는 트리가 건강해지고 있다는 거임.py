from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(now_node, par_node, k):
    global answer
    count_list = []
    for next_node in graph[now_node]:
        if next_node == par_node:
            continue
        else:
            count = dfs(next_node, now_node, k)
            if count == 0:
                continue
            count_list.append(count)
    count_list = sorted(count_list)
    total = node[now_node]

    idx = 0
    while idx < len(count_list) and total + count_list[idx] <= k:
        total += count_list[idx]
        idx += 1
    answer += len(count_list) - idx
    return total            

n, k = map(int, input().split())
node = list(map(int, input().split()))

graph = defaultdict(list)
answer = 0
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

dfs(0, 0, k)
print(answer)
