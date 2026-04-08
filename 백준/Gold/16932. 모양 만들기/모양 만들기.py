n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
dic = {}
dic[0] = 0
simbol = 1
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            stack = [[i, j]]
            simbol += 1
            count = 1
            matrix[i][j] = simbol
            while stack:
                now_i, now_j = stack.pop()
                for idx in range(4):
                    next_i = now_i + di[idx]
                    next_j = now_j + dj[idx]
                    if 0 <= next_i < n and 0 <= next_j < m and matrix[next_i][next_j] == 1:
                        stack.append([next_i, next_j])
                        matrix[next_i][next_j] = simbol
                        count += 1
            dic[simbol] = count

answer = 0
for i in range(n):
    for j in range(m):
        s = set()
        now_total = 1
        for idx in range(4):
            next_i = i + di[idx]
            next_j = j + dj[idx]
            if 0 <= next_i < n and 0 <= next_j < m:
                s.add(matrix[next_i][next_j])
        for simbol in s:
            now_total += dic[simbol]
        answer = max(answer, now_total)

print(answer)