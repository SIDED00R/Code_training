class Solution:
	def productExceptSelf(self, nums: list[int]) -> list[int]:
		prefix_product = [1]
		suffix_product = [1]
		
		prefix = 1
		suffix = 1
		for idx in range(len(nums)):
			prefix *= nums[idx]
			prefix_product.append(prefix)
			suffix *= nums[-idx - 1]
			suffix_product.append(suffix)
		
		answer = []
		for idx in range(len(nums)):
			front = prefix_product[idx]
			back = suffix_product[-idx - 2]
			answer.append(front * back)
		return answer