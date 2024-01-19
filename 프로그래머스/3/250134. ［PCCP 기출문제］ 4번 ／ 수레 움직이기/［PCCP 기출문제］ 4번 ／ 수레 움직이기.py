# 0: 빈칸, 1: 빨간 수레, 2: 파란 수레, 3: 빨간 도착, 4: 파란 도착, 5: 벽, 6: 빨간 지나감, 7: 파란 지나감
import copy
min_count = 40

def move(red, blue, maze, count, n, m, red_end, blue_end):
    global min_count
    r_i, r_j = red
    b_i, b_j = blue
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    if red == red_end and blue == blue_end:
        if min_count > count:
            min_count = count
        return min_count
    elif red == red_end:
        for b_idx in range(4):
            next_b_i = b_i + di[b_idx]
            next_b_j = b_j + dj[b_idx]
            if 0 <= next_b_i < n and 0 <= next_b_j < m and maze[next_b_i][next_b_j] not in [5, 7] and (r_i != next_b_i or r_j != next_b_j):
                copy_maze = copy.deepcopy(maze)
                if copy_maze[b_i][b_j] == 6:
                    copy_maze[b_i][b_j] = 5
                else:
                    copy_maze[b_i][b_j] = 7
                move(red, (next_b_i, next_b_j), copy_maze, count + 1, n, m, red_end, blue_end)     
    elif blue == blue_end:
        for r_idx in range(4):
            next_r_i = r_i + di[r_idx]
            next_r_j = r_j + dj[r_idx]
            if 0 <= next_r_i < n and 0 <= next_r_j < m and maze[next_r_i][next_r_j] not in [5, 6] and (next_r_i != b_i or next_r_j != b_j):
                copy_maze = copy.deepcopy(maze)
                if copy_maze[r_i][r_j] == 7:
                    copy_maze[r_i][r_j] = 5
                else:
                    copy_maze[r_i][r_j] = 6
                move((next_r_i, next_r_j), blue, copy_maze, count + 1, n, m, red_end, blue_end)
    else:
        for r_idx in range(4):
            for b_idx in range(4):
                next_r_i = r_i + di[r_idx]
                next_r_j = r_j + dj[r_idx]
                next_b_i = b_i + di[b_idx]
                next_b_j = b_j + dj[b_idx]
                if 0 <= next_r_i < n and 0 <= next_r_j < m and 0 <= next_b_i < n and 0 <= next_b_j < m and maze[next_r_i][next_r_j] not in [5, 6] and maze[next_b_i][next_b_j] not in [5, 7] and (next_r_i != next_b_i or next_r_j != next_b_j) and ((next_r_i, next_r_j) != blue or (next_b_i, next_b_j) != red):
                    copy_maze = copy.deepcopy(maze)
                    if copy_maze[r_i][r_j] == 7:
                        copy_maze[r_i][r_j] = 5
                    else:
                        copy_maze[r_i][r_j] = 6

                    if copy_maze[b_i][b_j] == 6:
                        copy_maze[b_i][b_j] = 5
                    else:
                        copy_maze[b_i][b_j] = 7
                    move((next_r_i, next_r_j), (next_b_i, next_b_j), copy_maze, count + 1, n, m, red_end, blue_end)
    return min_count

def solution(maze):
    n = len(maze)
    m = len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = (i, j)
            if maze[i][j] == 2:
                blue_start = (i, j)
            if maze[i][j] == 3:
                red_end = (i, j)
            if maze[i][j] == 4:
                blue_end = (i, j)
    
    answer = move(red_start, blue_start, maze, 0, n, m, red_end, blue_end)            
    return answer if answer != 40 else 0