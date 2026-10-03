class Solution:
	def twoSum(self, numbers: list[int], target: int) -> list[int]:
		for idx in range(len(numbers)):
			start = idx + 1
			end = len(numbers) - 1
			while start <= end:
				mid = (start + end) // 2
				now_num = numbers[idx] + numbers[mid]
				if now_num > target:
					end = mid - 1
				elif now_num < target:
					start = mid + 1
				else:
					return [idx + 1, mid + 1]