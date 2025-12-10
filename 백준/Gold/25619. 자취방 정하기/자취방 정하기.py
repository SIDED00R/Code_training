from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def find(n):
    visited = [False for _ in range(n + 1)]
    visited[1] = True
    stack = [1]
    answer = []
    loop = False
    while stack:
        out = stack.pop()
        for next_node in route[out]:
            if visited[next_node]:
                continue
            else:
                visited[next_node] = True
                answer.append(next_node)
                stack.append(next_node)
                if dic[(out, next_node)] < 0:
                    loop = True
    return answer, loop

def not_loop_find(n, answer_weight):
    weight = [1e20 for _ in range(n + 1)]
    weight[1] = 0
    stack = []
    heapq.heappush(stack, [0, 1])
    answer = set()
    answer.add(1)
    while stack:
        now_weight, idx = heapq.heappop(stack)
        if now_weight != weight[idx]:
            continue
        for next_node in route[idx]:
            next_weight = dic[(idx, next_node)] + now_weight
            if next_weight <= answer_weight and weight[next_node] > next_weight:
                weight[next_node] = next_weight
                heapq.heappush(stack, [next_weight, next_node])
                answer.add(next_node)
    return answer

            
n, m = map(int, input().split())
dic = {}
route = defaultdict(list)
for _ in range(m):
    u, v, a, b = map(int, input().split())
    w = (a + b) / 2
    dic[(u, v)] = w
    dic[(v, u)] = w
    route[u].append(v)
    route[v].append(u)
answer_weight = int(input())

able_node, loop = find(n)
if loop:
    print(len(able_node))
    for num in sorted(able_node):
        print(num, end = " ")
else:
    answer = not_loop_find(n, answer_weight)
    length = len(answer) - 1
    print(length)
    if length != 0:
        for num in sorted(answer)[1:]:
            print(num, end = " ")
        
