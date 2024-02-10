R, C = map(int, input().rstrip('\n').split())
board = []
for _ in range(R):
    line = list(input())
    board.append(line)

max_length = 0
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
visited = [False] * 26
visited[ord(board[0][0]) - 65] = True

def dfs(i, j, visited, count):
    global max_length
    max_length = max(max_length, count)
    for idx in range(4):
       next_i = di[idx] + i
       next_j = dj[idx] + j
       if 0 <= next_i < R and 0 <= next_j < C:
           next_node = board[next_i][next_j]
           if visited[ord(next_node) - 65] == False:
               visited[ord(next_node) - 65] = True
               dfs(next_i, next_j, visited, count + 1)
               visited[ord(next_node) - 65] = False

dfs(0, 0, visited, 1)

print(max_length)