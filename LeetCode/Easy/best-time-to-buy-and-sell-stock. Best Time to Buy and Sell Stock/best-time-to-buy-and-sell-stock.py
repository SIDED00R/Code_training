class Solution:
	def maxProfit(self, prices: list[int]) -> int:
		now_min = 1e10
		answer = 0
		for idx in range(len(prices)):
			now_min = min(now_min, prices[idx])
			answer = max(answer, prices[idx] - now_min)
		return answer