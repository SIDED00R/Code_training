class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		dic = {}
		for idx, now_num in enumerate(nums):
			if target - now_num in dic:
				return [dic[target - now_num], idx]
			dic[now_num] = idx