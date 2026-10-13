class Solution:
	def findContentChildren(self, g: list[int], s: list[int]) -> int:
		sort_g = sorted(g, reverse = True)
		sort_s = sorted(s, reverse = True)
		
		answer = 0
		while sort_g and sort_s:
			if sort_g[-1] <= sort_s[-1]:
				sort_g.pop()
				answer += 1
			sort_s.pop()
		return answer