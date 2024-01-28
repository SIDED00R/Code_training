import sys
input = sys.stdin.readline
import copy
 
N = int(input())
board = []
for _ in range(N):
    line = list(input().rstrip('\n'))
    board.append(line)
    
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


# normal people
normal_board = copy.deepcopy(board)
normal_count = 0
for i in range(N):
    for j in range(N):
        if normal_board[i][j] != 0:
            normal_count += 1
            now = normal_board[i][j]
            stack = [(i, j)]
            normal_board[i][j] = 0
            while stack:
                now_i, now_j = stack.pop()
                for idx in range(4):
                    next_i, next_j = now_i + di[idx], now_j + dj[idx]
                    if 0 <= next_i < N and 0 <= next_j < N and normal_board[next_i][next_j] == now:
                        normal_board[next_i][next_j] = 0
                        stack.append((next_i, next_j))
    
                        
# odd people
odd_board = copy.deepcopy(board)
odd_count = 0
for i in range(N):
    for j in range(N):
        if odd_board[i][j] != 0:
            odd_count += 1
            now = odd_board[i][j]
            stack = [(i, j)]
            odd_board[i][j] = 0
            if now == "B":
                while stack:
                    now_i, now_j = stack.pop()
                    for idx in range(4):
                        next_i, next_j = now_i + di[idx], now_j + dj[idx]
                        if 0 <= next_i < N and 0 <= next_j < N and odd_board[next_i][next_j] == now:
                            odd_board[next_i][next_j] = 0
                            stack.append((next_i, next_j))
            else:
                while stack:
                    now_i, now_j = stack.pop()
                    for idx in range(4):
                        next_i, next_j = now_i + di[idx], now_j + dj[idx]
                        if 0 <= next_i < N and 0 <= next_j < N and (odd_board[next_i][next_j] == "R" or odd_board[next_i][next_j] == "G"):
                            odd_board[next_i][next_j] = 0
                            stack.append((next_i, next_j))
                            
print(normal_count, odd_count)
            