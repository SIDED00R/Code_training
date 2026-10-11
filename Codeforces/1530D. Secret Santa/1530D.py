from collections import defaultdict

t = int(input())
for _ in range(t):
	k = int(input())
	line = list(map(int, input().split()))
	dic_from = defaultdict(list)
	dic_go = {}
	for idx in range(k):
		dic_from[line[idx]].append(idx + 1)
		dic_go[idx + 1] = line[idx]
		
	start = []
	target = {}
	for idx in range(1, k + 1):
		if len(dic_from[idx]) == 0:
			target[idx] = 1
		elif len(dic_from[idx]) > 1:
			for now_case in dic_from[idx]:
				if dic_from[now_case] == []:
					break
			for check in dic_from[idx]:
				if check != now_case:
					start.append(check)
	
	same = []
	start_list = []
	for start_node in start:
		if start_node in target:
			same.append(start_node)
			target.pop(start_node)
		else:
			start_list.append(start_node)
	
	if len(same) == 1:
		key, v = target.popitem()
		dic_go[same[0]] = key
		target[same[0]] = 1
	elif len(same) > 1:
		for idx in range(len(same)):
			s = same[idx]
			e = same[(idx + 1) % len(same)]
			dic_go[s] = e
	
	idx = 0
	for key, v in target.items():
		s = start_list[idx]
		e = key
		dic_go[s] = e
		idx += 1
	print(k - len(start))
	answer = []
	for idx in range(1, k + 1):
		answer.append(str(dic_go[idx]))
	print(" ".join(answer))