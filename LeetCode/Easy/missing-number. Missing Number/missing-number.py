class Solution:
	def missingNumber(self, nums: list[int]) -> int:
		sorted_num = sorted(nums)
		for i in range(len(nums)):
			if i != sorted_num[i]:
				return i
		return len(nums)