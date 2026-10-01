class Solution:
	def mySqrt(self, x: int) -> int:
		min_num = 0
		max_num = 2 ** 32
		while min_num <= max_num:
			mid = (min_num + max_num) // 2
			if mid ** 2 > x:
				max_num = mid - 1
			else:
				min_num = mid + 1
		return max_num