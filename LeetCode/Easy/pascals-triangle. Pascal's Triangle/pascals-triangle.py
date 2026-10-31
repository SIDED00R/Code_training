class Solution:
	def generate(self, numRows: int) -> list[list[int]]:
		answer = []
		for i in range(numRows):
			if i == 0:
				answer.append([1])
			elif i == 1:
				answer.append([1, 1])
			else:
				now_ans = [1]
				for j in range(i - 1):
					now_ans.append(answer[-1][j] + answer[-1][j + 1])
				now_ans.append(1)
				answer.append(now_ans)
		return answer