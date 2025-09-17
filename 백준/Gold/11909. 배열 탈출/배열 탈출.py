import heapq

def dijkstra(start, end, n, weight):
    distances = { (i, j): float('inf') for i in range(n) for j in range(n) }
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, current_node = heapq.heappop(pq)

        if dist > distances[current_node]:
            continue

        if current_node == end:
            return distances[end]

        x, y = current_node

        for dx, dy in [(0, 1), (1, 0)]: 
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n:
                next_node = (nx, ny)
                edge_weight = weight.get((x, y, nx, ny), float('inf'))

                if edge_weight != float('inf'):
                    new_dist = dist + edge_weight
                    if new_dist < distances[next_node]:
                        distances[next_node] = new_dist
                        heapq.heappush(pq, (new_dist, next_node))
    
    return float('inf')
    
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

INF = 10**18
prev_row = [INF] * n 
for i in range(n):
    cur_row = [INF] * n
    for j in range(n):
        if i == 0 and j == 0:
            cur_row[j] = 0
            continue

        if i > 0:
            down_cost = max(matrix[i][j] - matrix[i-1][j] + 1, 0)
            cur_row[j] = min(cur_row[j], prev_row[j] + down_cost)

        if j > 0:
            right_cost = max(matrix[i][j] - matrix[i][j-1] + 1, 0)
            cur_row[j] = min(cur_row[j], cur_row[j-1] + right_cost)

    prev_row = cur_row  

print(prev_row[-1])