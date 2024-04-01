import sys
import copy

input = sys.stdin.readline
answer = 0

def move(board, idx):
    n = len(board)
    new_board = copy.deepcopy(board)
    merged = [[False] * n for _ in range(n)]
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, 1, -1]
    
    if idx == 0:
        range_i = range(1, n)
        range_j = range(n)
    elif idx == 1: 
        range_i = range(n-2, -1, -1)
        range_j = range(n)
    elif idx == 2: 
        range_i = range(n)
        range_j = range(n-2, -1, -1)
    else: 
        range_i = range(n)
        range_j = range(1, n)
        
    for i in range_i:
        for j in range_j:
            if new_board[i][j] != 0:
                now_i, now_j = i, j
                while True:
                    next_i, next_j = now_i + di[idx], now_j + dj[idx]
                    if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n or (new_board[next_i][next_j] != 0 and not (new_board[next_i][next_j] == new_board[i][j] and not merged[next_i][next_j])):
                        break
                    now_i, now_j = next_i, next_j
                if (now_i, now_j) != (i, j):
                    if new_board[now_i][now_j] == 0:
                        new_board[now_i][now_j] = new_board[i][j]
                    elif new_board[now_i][now_j] == new_board[i][j]:
                        new_board[now_i][now_j] *= 2
                        merged[now_i][now_j] = True
                    new_board[i][j] = 0

    return new_board

def find_case(board, count):
    global answer
    for idx in range(4):
        new_board = move(board, idx)
        if count < 4:
            find_case(new_board, count + 1)
        max_value = max(max(row) for row in new_board)
        if max_value > answer:
            answer = max_value

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
find_case(board, 0)
print(answer)
