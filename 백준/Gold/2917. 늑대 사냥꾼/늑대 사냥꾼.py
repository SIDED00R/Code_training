import heapq

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(input())
    matrix.append(line)

count_matrix = [[-1 for _ in range(m)] for _ in range(n)]
tree_list = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "+":
            count_matrix[i][j] = 0
            heapq.heappush(tree_list, [0, i, j])
        elif matrix[i][j] == "V":
            start = [i, j]
        elif matrix[i][j] == "J":
            end = [i, j]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
while tree_list:
    weight, i, j = heapq.heappop(tree_list)
    for idx in range(4):
        ni = di[idx] + i
        nj = dj[idx] + j
        if 0 <= ni < n and 0 <= nj < m and count_matrix[ni][nj] == -1:
            count_matrix[ni][nj] = weight + 1
            heapq.heappush(tree_list, [weight + 1, ni, nj])

answer = count_matrix[start[0]][start[1]]
next_able = []
visited = [[False for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]] = True
heapq.heappush(next_able, [-answer, start[0], start[1]])
while True:
    weight, i, j = heapq.heappop(next_able)
    answer = min(-weight, answer)
    if [i, j] == end:
        break
    for idx in range(4):
        ni = di[idx] + i
        nj = dj[idx] + j
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
            visited[ni][nj] = True
            heapq.heappush(next_able, [-count_matrix[ni][nj], ni, nj])
print(answer)