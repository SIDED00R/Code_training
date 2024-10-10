from collections import deque

n, m, k = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
answer = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            stack = deque()
            stack.append([i, j])
            matrix[i][j] = 1
            count = 1
            while stack:
                now_i, now_j = stack.popleft()
                for idx in range(4):
                    ni = now_i + di[idx]
                    nj = now_j + dj[idx]
                    if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 0:
                        matrix[ni][nj] = 1
                        count += 1
                        stack.append([ni, nj])
            answer += count // k
            if count % k != 0:
                answer += 1
if answer > m or answer == 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(m - answer)