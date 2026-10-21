from collections import defaultdict

class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		dic = defaultdict(int)
		dic[0] = 1

		p_sum = 0
		answer = 0

		for num in nums:
			p_sum += num
			answer += dic[p_sum - k]
			dic[p_sum] += 1

		return answer