class Solution:
	def longestPalindrome(self, s: str) -> str:
		new_s = "#"
		for letter in s:
			new_s += letter + "#"
		
		length = len(new_s)
		dp = [0] * length
		
		center = 0
		right = 0
		max_length = 0
		max_center = 0
		
		for i in range(length):
			if i < right:
				mirror = 2 * center - i
				dp[i] = min(right - i, dp[mirror])
			
			while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < length and new_s[i - dp[i] - 1] == new_s[i + dp[i] + 1]:
				dp[i] += 1
			if i + dp[i] > right:
				center = i
				right = i + dp[i]
			if dp[i] > max_length:
				max_length = dp[i]
				max_center = i
				
		start = (max_center - max_length) // 2
		return s[start:start + max_length]