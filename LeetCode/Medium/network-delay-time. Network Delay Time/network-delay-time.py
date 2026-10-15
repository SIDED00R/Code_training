from collections import defaultdict

class Solution:
	def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
		route = defaultdict(list)
		weight = {}
		for time in times:
			u, v, w = time
			route[u].append(v)
			weight[(u, v)] = w
		visited = [-1] * (n + 1)	
		stack = [k]
		visited[k] = 0
		while stack:
			now_node = stack.pop()
			for next_node in route[now_node]:
				w = weight[(now_node, next_node)]
				if visited[next_node] == -1 or visited[next_node] > visited[now_node] + w:
					visited[next_node] = visited[now_node] + w
					stack.append(next_node)
		answer = -1
		for ans_time in visited[1:]:
			if ans_time == -1:
				return -1
			answer = max(answer, ans_time)		
		return answer