from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def check(now_node):
    global answer
    if answer[1] < weight[now_node]:
        answer = [now_node, weight[now_node]]
    elif answer[1] == weight[now_node]:
        answer[0] = min(answer[0], now_node)

    first_idx = now_node
    first_max = 0
    second_idx = now_node
    second_max = 0
    
    for next_node in route[now_node]:
        if not visited[next_node]:
            visited[next_node] = True
            idx, w = check(next_node)
            if w > first_max or (w == first_max and idx < first_idx):
                second_idx, second_max = first_idx, first_max
                first_idx, first_max = idx, w
            elif w > second_max or (w == second_max and idx < second_idx):
                second_idx, second_max = idx, w
                
    total = weight[now_node] + first_max + second_max
    start = min(first_idx, second_idx)

    if answer[1] < total:
        answer = [start, total]
    elif answer[1] == total:
        answer[0] = min(answer[0], start)

    return first_idx, first_max + weight[now_node]

n = int(input())
weight = list(map(int, input().split()))
route = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    route[a].append(b)
    route[b].append(a)

visited = [False for _ in range(n)]
answer = [0, weight[0]]
visited[0] = True
check(0)
print(answer[1], answer[0] + 1)


