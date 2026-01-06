import sys
from collections import defaultdict
input = sys.stdin.readline

k = int(input())
change = {1:0, 0:1}
for _ in range(k):
    answer = True
    node = defaultdict(list)
    v, e = map(int, input().split())
    color = [-1 for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    for idx in range(1, v + 1):
        if color[idx] == -1:
            stack = [idx]
            color[idx] = 0
            while stack:
                out = stack.pop()
                next_color = change[color[out]]
                for next_node in node[out]:
                    if color[next_node] == next_color:
                        continue
                    elif color[next_node] == -1:
                        stack.append(next_node)
                        color[next_node] = next_color
                    else:
                        answer = False
                        stack = []
                        break
    if answer:
        print("YES")
    else:
        print("NO")
    
