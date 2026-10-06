class Solution:
	def reverse(self, x: int) -> int:
		
		s_int = str(x)
		if s_int[0] == "-":
			answer = "-" + s_int[1:][::-1]
		else:
			answer = s_int[::-1]
		
		answer = int(answer)
		if -2**31 <= answer <= 2**31 - 1:
			return answer
		else:
			return 0