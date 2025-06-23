n, m = map(int, input().split())
matrix = []
for _ in range(m):
    line = list(input())
    matrix.append(line)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
dic = {'W':0, 'B':0}
for i in range(m):
    for j in range(n):
        simbol = matrix[i][j]
        if simbol == '':
            continue
        else:
            count = 1
            matrix[i][j] = ''
            stack = [[i, j]]
            while stack:
                now_i, now_j = stack.pop()
                for idx in range(4):
                    ni = now_i + di[idx]
                    nj = now_j + dj[idx]
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] == simbol:
                        matrix[ni][nj] = ''
                        count += 1
                        stack.append([ni, nj])
            dic[simbol] += count ** 2

print(dic['W'], dic['B'])
            