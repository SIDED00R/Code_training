import heapq

class Solution:
	def swimInWater(self, grid: list[list[int]]) -> int:
		row = len(grid)
		col = len(grid[0])
		weight = [[10000 for _ in range(col)] for _ in range(row)]
		
		heap = []
		heapq.heappush(heap, [grid[0][0], 0, 0])
		weight[0][0] = grid[0][0]

		di = [0, 0, 1, -1]
		dj = [1, -1, 0, 0]
		
		while heap:
			w, i, j = heapq.heappop(heap)
			for idx in range(4):
				ni = i + di[idx]
				nj = j + dj[idx]
				if 0 <= ni < row and 0 <= nj < col and weight[ni][nj] == 10000:
					weight[ni][nj] = max(grid[ni][nj], w)
					heapq.heappush(heap, [weight[ni][nj], ni, nj])
		return weight[-1][-1]