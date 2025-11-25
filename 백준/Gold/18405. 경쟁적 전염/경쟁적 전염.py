import heapq, copy

n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

stack = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            heapq.heappush(stack, [matrix[i][j], i, j])

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for _ in range(s):
    next_stack = []
    while stack:
        num, i, j = heapq.heappop(stack)
        for idx in range(4):
            next_i = i + di[idx]
            next_j = j + dj[idx]
            if 0 <= next_i < n and 0 <= next_j < n and matrix[next_i][next_j] == 0:
                matrix[next_i][next_j] = num
                heapq.heappush(next_stack, [num, next_i, next_j])
    stack = copy.deepcopy(next_stack)

print(matrix[x - 1][y - 1])