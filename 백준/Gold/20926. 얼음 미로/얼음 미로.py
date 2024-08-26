import heapq

w, h = map(int, input().split())
matrix = []

for _ in range(h):
    matrix.append(list(input()))
    
for i in range(h):
    for j in range(w):
        if matrix[i][j] == "T":
            start = [0, i, j]
            matrix[i][j] = "0"
            
heap = []
heapq.heappush(heap, start)

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

visited_matrix = [[1e9 for _ in range(w)] for _ in range(h)]

answer = 1e9
while heap:
    count, i, j = heapq.heappop(heap)
    if count >= answer:
        break
    for idx in range(4):
        total = 0
        ni = i + di[idx]
        nj = j + dj[idx]
        while 0 <= ni < h and 0 <= nj < w:
            if matrix[ni][nj] == "E":
                answer = min(answer, total + count)
                break
            elif matrix[ni][nj] == "H":
                break
            elif matrix[ni][nj] == "R":
                stop_i = ni - di[idx]
                stop_j = nj - dj[idx]
                if visited_matrix[stop_i][stop_j] > count + total:
                    visited_matrix[stop_i][stop_j] = count + total
                    heapq.heappush(heap, [count + total, stop_i, stop_j])
                break
            else:
                total += int(matrix[ni][nj])
            ni += di[idx]
            nj += dj[idx]
            
if answer >= 1e8:
    print(-1)
else:
    print(answer)
                
    
    