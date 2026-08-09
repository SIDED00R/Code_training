di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    
    answer = True
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "B":
                for idx in range(4):
                    ni = i + di[idx]
                    nj = j + dj[idx]
                    if 0 <= ni < n and 0 <= nj < m:
                        if matrix[ni][nj] == "G":
                            answer = False
                        elif matrix[ni][nj] == ".":
                            matrix[ni][nj] = "#"
    if matrix[n - 1][m - 1] != "#":
        stack = [[n - 1, m - 1]]
        matrix[n - 1][m - 1] = "#"
        while stack:
            i, j = stack.pop()
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] != "#":
                    stack.append([ni, nj])
                    matrix[ni][nj] = "#"
    for l in matrix:
        if "G" in l:
            answer = False
    if not answer :
        print("No")
    else:
        print("Yes")