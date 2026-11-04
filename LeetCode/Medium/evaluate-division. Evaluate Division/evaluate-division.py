from collections import defaultdict

class Solution:
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
		route = defaultdict(list)
		weight = defaultdict(int)
		for i in range(len(equations)):
			front, back = equations[i]
			value = values[i]		   
			route[front].append(back)
			route[back].append(front)
			weight[(front, back)] = value
			weight[(back, front)] = 1 / value
		answer = []
		for query in queries:
			front, back = query
			now_weight = {}
			now_weight[front] = 1
			stack = [front]
			find = False
			while stack and not find:
				now_node = stack.pop()
				for next_node in route[now_node]:
					if next_node == back:
						find = True
						answer.append(now_weight[now_node] * weight[(now_node, next_node)])
						break
					if next_node not in now_weight:
						now_weight[next_node] = now_weight[now_node] * weight[(now_node, next_node)]
						stack.append(next_node)
			if not find:
				answer.append(-1)
		return answer