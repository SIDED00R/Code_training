class Solution:
	def minSubArrayLen(self, target: int, nums: list[int]) -> int:
		p_sum = [0]
		for i in range(len(nums)):
			p_sum.append(p_sum[-1] + nums[i])
		answer = 1e9
		front_point = 1
		back_point = 0
		while front_point <= len(nums):
			front_num = p_sum[front_point]
			back_num = p_sum[back_point]
			if front_num - back_num >= target:
				answer = min(answer, front_point - back_point)
				back_point += 1
			else:
				front_point += 1
		if answer == 1e9:
			return 0
		return answer