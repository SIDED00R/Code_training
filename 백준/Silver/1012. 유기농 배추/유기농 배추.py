import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    answer = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                answer += 1
                stack = []
                stack.append([i, j])
                while stack:
                    now_i, now_j = stack.pop()
                    ground[now_i][now_j] = 0
                    for idx in range(4):
                        next_i = now_i + dx[idx]
                        next_j = now_j + dy[idx]
                        if next_i >= 0 and next_i < N and next_j >= 0 and next_j < M and ground[next_i][next_j] == 1:
                            stack.append([next_i, next_j])
    print(answer)
                
            