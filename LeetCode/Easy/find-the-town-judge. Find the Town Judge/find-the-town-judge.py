from collections import defaultdict

class Solution:
	def findJudge(self, n: int, trust: list[list[int]]) -> int:
		if n == 1:
			return 1
		dic = defaultdict(int)
		point = defaultdict(int)
		for a, b in trust:
			dic[b] += 1
			point[a] += 1
		
		answer = -1
		for k, v in dic.items():
			if v == n - 1 and point[k] == 0:
				if answer == -1:
					answer = k
				else:
					return -1
		return answer