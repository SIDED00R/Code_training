import heapq

dp = [[0 for _ in range(502)] for _ in range(502)]
d_dp = [[0 for _ in range(502)] for _ in range(502)]

def sliding_sum(matrix):

    length = len(matrix)
    for i in range(length):
        for j in range(1, length):
            matrix[i][j] += matrix[i][j - 1]

    for j in range(length):
        for i in range(1, length):
            matrix[i][j] += matrix[i - 1][j]

    return matrix

n = int(input())
for _ in range(n):
    X1, Y1, X2, Y2 = map(int, input().split())
    sx = min(X1, X2)
    lx = max(X1, X2)
    sy = min(Y1, Y2)
    ly = max(Y1, Y2)
    dp[sx][sy] += 1
    dp[lx + 1][ly + 1] += 1
    dp[sx][ly + 1] -= 1
    dp[lx + 1][sy] -= 1

m = int(input())
for _ in range(m):
    X1, Y1, X2, Y2 = map(int, input().split())
    sx = min(X1, X2)
    lx = max(X1, X2)
    sy = min(Y1, Y2)
    ly = max(Y1, Y2)
    d_dp[sx][sy] += 1
    d_dp[lx + 1][ly + 1] += 1
    d_dp[sx][ly + 1] -= 1
    d_dp[lx + 1][sy] -= 1

dp = sliding_sum(dp)
d_dp = sliding_sum(d_dp)

for i in range(502):
    for j in range(502):
        if d_dp[i][j] == 0:
            continue
        else:
            dp[i][j] = -1

answer = [[3000000 for _ in range(501)] for _ in range(501)]
answer[0][0] = 0
heap = []
heapq.heappush(heap, [0, 0, 0])
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

while heap and answer[-1][-1] == 3000000:
    w, i, j = heapq.heappop(heap)
    for idx in range(4):
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0 <= ni < 501 and 0 <= nj < 501 and dp[ni][nj] != -1:
            if dp[ni][nj] == 0:
                if answer[ni][nj] > w:
                    answer[ni][nj] = w
                    heapq.heappush(heap, [w, ni, nj])
            else:
                if answer[ni][nj] > w + 1:
                    answer[ni][nj] = w + 1
                    heapq.heappush(heap, [w + 1, ni, nj])


ans = answer[-1][-1]
if ans == 3000000:
    print(-1)
else:
    print(ans)
