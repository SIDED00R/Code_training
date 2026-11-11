class Solution:
	def minCostClimbingStairs(self, cost: list[int]) -> int:
		answer = [0] * len(cost)
		answer[0] = cost[0]
		answer[1] = cost[1]
		for i in range(2, len(cost)):
			answer[i] = cost[i] + min(answer[i-2:i])
		return min(answer[-2:])