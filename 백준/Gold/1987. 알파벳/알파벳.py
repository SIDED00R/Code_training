R, C = map(int, input().rstrip('\n').split())
board = []
for _ in range(R):
    line = list(input())
    board.append(line)

max_length = 0
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

stack = set()
stack.add((0, 0, board[0][0]))
while stack:
    i, j, now = stack.pop()
    max_length = max(max_length, len(now))
    if max_length == 26:
        print(26)
        exit()
    for idx in range(4):
        next_i = i + di[idx]
        next_j = j + dj[idx]
        if 0 <= next_i < R and 0 <= next_j < C:
            if board[next_i][next_j] not in set(now):
                next_node = board[next_i][next_j]
                stack.add((next_i, next_j, now + next_node))

print(max_length)