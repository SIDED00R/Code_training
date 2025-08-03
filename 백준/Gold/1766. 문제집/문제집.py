from collections import defaultdict
import heapq

n, m = map(int, input().split())
dic = defaultdict(list)
count_dic = defaultdict(int)
top = [True for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    top[b] = False
    dic[a].append(b)
    count_dic[b] += 1

answer = []

for idx in range(1, n + 1):
    if top[idx] == True:
        stack = []
        heapq.heappush(stack, idx)
        while stack:
            out = heapq.heappop(stack)
            answer.append(out)
            for next_node in dic[out]:
                count_dic[next_node] -= 1
                if count_dic[next_node] == 0:
                    heapq.heappush(stack, next_node)

for num in answer:
    print(num, end = " ")

        