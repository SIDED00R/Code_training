n = int(input())
matrix = []
visited_matrix = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    matrix.append(input().split())
    
answer = "0b"
answer += matrix[0][0]
stack = [[0, 0]]

for i in range(2 * n - 2):
    one = []
    zero = []
    for case in stack:
        now_i, now_j = case
        for di, dj in [[1, 0], [0, 1]]:
            next_i, next_j = now_i + di, now_j + dj
            if next_i < n and next_j < n and not visited_matrix[next_i][next_j]:
                visited_matrix[next_i][next_j] = True
                if matrix[next_i][next_j] == "1":
                    one.append([next_i, next_j])
                else:
                    zero.append([next_i, next_j])
    if one:
        stack = one[:]
        answer += "1"
    else:
        stack = zero[:]
        answer += "0"
        
print(int(answer, 2))
    