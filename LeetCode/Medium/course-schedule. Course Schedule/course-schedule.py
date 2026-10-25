from collections import defaultdict

class Solution:
	def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
		count = defaultdict(int)
		next_node = defaultdict(list)

		for prerequisite in prerequisites:
			front, back = prerequisite
			next_node[front].append(back)
			count[back] += 1
		
		stack = []
		for i in range(numCourses):
			if count[i] == 0:
				stack.append(i)

		while stack:
			out = stack.pop()
			for n_n in next_node[out]:
				count[n_n] -= 1
				if count[n_n] == 0:
					stack.append(n_n)

		for k, v in count.items():
			if v != 0:
				return False
		return True