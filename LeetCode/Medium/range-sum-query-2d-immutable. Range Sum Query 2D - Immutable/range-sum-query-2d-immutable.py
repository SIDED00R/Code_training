class NumMatrix:

	def __init__(self, matrix: list[list[int]]):
		row = len(matrix)
		col = len(matrix[0])
		self.p_sum = []
		for i in range(row):
			now_p = []
			total = 0
			for j in range(col):
				total += matrix[i][j]
				now_p.append(total)
			self.p_sum.append(now_p)
		
		for j in range(col):
			for i in range(1, row):
				self.p_sum[i][j] += self.p_sum[i - 1][j]

	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
		answer = self.p_sum[row2][col2]
		if row1 > 0 and col1 > 0:
			answer = answer + self.p_sum[row1 - 1][col1 - 1] - self.p_sum[row2][col1 - 1] - self.p_sum[row1 - 1][col2]
		elif row1 > 0:
			answer = answer - self.p_sum[row1 - 1][col2]
		elif col1 > 0:
			answer = answer - self.p_sum[row2][col1 - 1]
		return answer
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)