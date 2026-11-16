class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		count = [0] * 26
		left = 0
		max_count = 0
		answer = 0

		for right in range(len(s)):
			idx = ord(s[right]) - ord('A')
			count[idx] += 1
			max_count = max(max_count, count[idx])

			if (right - left + 1) - max_count > k:
				count[ord(s[left]) - ord('A')] -= 1
				left += 1

			answer = max(answer, right - left + 1)

		return answer