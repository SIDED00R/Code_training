class Solution:
	def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
		row = len(matrix)
		col = len(matrix[0])

		di = [0, 0, 1, -1]
		dj = [1, -1, 0, 0]

		dp = [[0] * col for _ in range(row)]

		def dfs(i, j):
			if dp[i][j] != 0:
				return dp[i][j]

			dp[i][j] = 1

			for idx in range(4):
				ni = i + di[idx]
				nj = j + dj[idx]

				if (0 <= ni < row and
					0 <= nj < col and
					matrix[ni][nj] > matrix[i][j]):

					dp[i][j] = max(
						dp[i][j],
						dfs(ni, nj) + 1
					)

			return dp[i][j]

		answer = 0
		for i in range(row):
			for j in range(col):
				answer = max(answer, dfs(i, j))

		return answer