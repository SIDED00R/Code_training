class Solution:
	def wordBreak(self, s: str, wordDict: list[str]) -> bool:
		dp = [0 for _ in range(len(s) + 1)]
		dp[0] = 1
		for i in range(1, len(s) + 1):
			for word in wordDict:
				word_length = len(word)
				if i - word_length >= 0 and dp[i - word_length] == 1 and s[i - word_length:i] == word:
					dp[i] = 1
					break
		if dp[-1]:
			return True
		else:
			return False