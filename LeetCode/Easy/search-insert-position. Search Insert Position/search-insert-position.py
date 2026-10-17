class Solution:
	def searchInsert(self, nums: list[int], target: int) -> int:
		front = 0
		back = len(nums) - 1
		while front <= back:
			mid = (front + back) // 2
			if nums[mid] < target:
				front = mid + 1
			else:
				back = mid - 1
		return front