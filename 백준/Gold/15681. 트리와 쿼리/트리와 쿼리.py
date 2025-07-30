from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def find(now_node, dic):
    global visited, answer
    last = True
    for next_node in dic[now_node]:
        if not visited[next_node]:
            last = False
            visited[next_node] = True
            answer[now_node] += find(next_node, dic)
    if last:
        return 1
    else:
        return answer[now_node] + 1

n, r, q = map(int, input().split())
dic = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    dic[u].append(v)
    dic[v].append(u)

answer = [0] * (n + 1)
visited = [False] * (n + 1)
visited[r] = True

find(r, dic)

for _ in range(q):
    now = int(input())
    print(answer[now] + 1)