from collections import defaultdict

n = int(input())
route = defaultdict(list)
dic = {}
for idx in range(n - 1):
	u, v = map(int, input().split())
	route[u].append(v)
	route[v].append(u)
	dic[(min(u, v), max(u, v))] = idx
	
find_idx = -1
for idx in range(1, n + 1):
	if len(route[idx]) >= 3:
		find_idx = idx
		break
if find_idx == -1:
	for i in range(n - 1):
		print(i)
else:
	answer = [-1] * (n - 1)
	count = 0
	for next_node in route[find_idx][:3]:
		u, v = min(next_node, find_idx), max(next_node, find_idx)
		idx = dic[(u, v)]
		answer[idx] = count
		count += 1
	for i in range(n - 1):
		if answer[i] == -1:
			answer[i] = count
			count += 1
	for ans in answer:
		print(ans)