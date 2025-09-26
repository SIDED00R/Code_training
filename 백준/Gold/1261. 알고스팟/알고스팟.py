def move(matrix, stack, n, m, answer):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    while True:
        next_stack = []
        for now_node in stack:
            i, j = now_node
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] != -1:
                    if matrix[ni][nj] == '0':
                        stack.append((ni, nj))
                    elif matrix[ni][nj] == '1':
                        next_stack.append((ni, nj))
                    matrix[ni][nj] = -1
        if matrix[-1][-1] != '0':
            break
        else:
            answer += 1
            stack = next_stack[:]
    return answer
                        
m, n = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(input())
    matrix.append(line)
matrix[0][0] = -1
print(move(matrix, [(0, 0)], n, m, 0))