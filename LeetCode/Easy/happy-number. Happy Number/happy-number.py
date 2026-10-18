class Solution:
	def isHappy(self, n: int) -> bool:
		dic = {}
		dic[n] = 1
		while True:
			str_num = str(n)
			total = 0
			for num in str_num:
				total += int(num) ** 2
			if total == 1:
				return True
			if total in dic:
				return False
			else:
				dic[total] = 1
				n = total