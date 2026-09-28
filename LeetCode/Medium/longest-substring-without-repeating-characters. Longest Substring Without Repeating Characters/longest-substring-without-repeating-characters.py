from collections import deque, defaultdict

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		stack = deque()
		dic = defaultdict(int)
		answer = 0
		for letter in s:
			stack.append(letter)
			dic[letter] += 1
			while dic[letter] > 1:
				out = stack.popleft()
				dic[out] -= 1
			answer = max(answer, len(stack))
		return answer