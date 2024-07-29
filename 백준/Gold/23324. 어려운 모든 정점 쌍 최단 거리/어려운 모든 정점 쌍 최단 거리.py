from collections import defaultdict

n, m, k = map(int, input().split())
dic = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    if i == k - 1:
        continue
    else:
        dic[u].append(v)
        dic[v].append(u)
        
visit = [False] * (n + 1)
visit[1] = True
stack = [1]
count = 1
while stack:
    now = stack.pop()
    for case in dic[now]:
        if visit[case]:
            continue
        else:
            stack.append(case)
            visit[case] = True
            count += 1
            
print(count * (n - count))