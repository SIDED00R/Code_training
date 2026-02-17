n, m = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
matrix = []
for _ in range(n):
    matrix.append(list(input()))

answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        else:
            visited[i][j] = 1
            answer += 1
            sim = matrix[i][j]
            if sim == "-":
                for now_j in range(j + 1, m):
                    if matrix[i][now_j] == "-":
                        visited[i][now_j] = 1
                    else:
                        break
            if sim == "|":
                for now_i in range(i + 1, n):
                    if matrix[now_i][j] == "|":
                        visited[now_i][j] = 1
                    else:
                        break
                        
print(answer)