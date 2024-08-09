from collections import deque

t = int(input())
di = [2, 1, -1, -2, -2, -1, 1, 2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]
for _ in range(t):
    l = int(input())
    visited_matrix = [[False for _ in range(l)] for _ in range(l)]
    now_i, now_j = map(int, input().split())
    end_i, end_j = map(int, input().split())
    stack = deque([[now_i, now_j, 0]])
    visited_matrix[now_i][now_j] = True
    if now_i == end_i and now_j == end_j:
        print(0)
        continue
    find = False
    while not find:
        i, j, count = stack.popleft()
        for idx in range(8):
            ni, nj = i + di[idx], j + dj[idx]
            if 0 <= ni < l and 0 <= nj < l and not visited_matrix[ni][nj]:
                if ni == end_i and nj == end_j:
                    find = True
                    print(count + 1)
                    break
                visited_matrix[ni][nj] = True
                stack.append([ni, nj, count + 1])
        
    
    