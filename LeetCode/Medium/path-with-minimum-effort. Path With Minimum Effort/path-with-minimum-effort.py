import heapq

class Solution:
	def minimumEffortPath(self, heights: list[list[int]]) -> int:
		row = len(heights)
		col = len(heights[0])
		di = [0, 0, -1, 1]
		dj = [1, -1, 0, 0]
		visited = [[1e9 for _ in range(col)] for _ in range(row)]
		visited[0][0] = 0
		
		heap = []
		heapq.heappush(heap, [0, 0, 0]) # weight, i, j
		answer = 0
		while heap:
			weight, i, j = heapq.heappop(heap)
			answer = max(answer, weight)
			if i == row - 1 and j == col - 1:
				return answer
			for idx in range(4):
				ni = i + di[idx]
				nj = j + dj[idx]
				if 0 <= ni < row and 0 <= nj < col:
					diff = abs(heights[i][j] - heights[ni][nj])
					if diff < visited[ni][nj]:
						visited[ni][nj] = diff
						heapq.heappush(heap, [diff, ni, nj])