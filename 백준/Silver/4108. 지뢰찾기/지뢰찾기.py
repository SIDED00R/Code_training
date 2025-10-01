while True:
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    r, c = map(int, input().split())
    if r == c == 0:
        break
    matrix = []
    for _ in range(r):
        line = list(input())
        matrix.append(line)
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == '.':
                count = 0
                for idx in range(8):
                    ni = i + di[idx]
                    nj = j + dj[idx]
                    if 0 <= ni < r and 0 <= nj < c and matrix[ni][nj] == '*':
                        count += 1
                matrix[i][j] = count

    for l in matrix:
        for num in l:
            print(num, end = "")
        print()