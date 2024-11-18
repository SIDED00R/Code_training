from collections import deque
import sys
input = sys.stdin.readline 

def find(x):
	if parent_node[x] != x:
		ans = find(parent_node[x])
		parent_node[x] = ans
		return ans
	else:
		return x

def union(a, b):
	global count
	a = find(a)
	b = find(b)
	if a < b:
		parent_node[b] = a
		count += 1
	elif b < a:
		parent_node[a] = b
		count += 1
	else:
		parent_node[a] = b

	
count = 0
n, k = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]
weight_matrix = [[-1 for _ in range(n)] for _ in range(n)]
stack = deque([])
for i in range(k):
	x, y = map(int, input().split())
	matrix[x - 1][y - 1] = i + 1
	stack.append([x - 1, y - 1])
	weight_matrix[x - 1][y - 1] = 0

parent_node = [idx for idx in range(k + 1)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
while stack:
	i, j = stack.popleft()
	for idx in range(4):
		ni = i + di[idx]
		nj = j + dj[idx]
		if 0 <= ni < n and 0 <= nj < n:
			if matrix[ni][nj] == 0:
				stack.append([ni, nj])
				weight_matrix[ni][nj] = weight_matrix[i][j] + 1
				matrix[ni][nj] = matrix[i][j]
			else:
				union(matrix[i][j], matrix[ni][nj])
				if count == k - 1:
					print(max(weight_matrix[ni][nj], weight_matrix[i][j]))
					exit()