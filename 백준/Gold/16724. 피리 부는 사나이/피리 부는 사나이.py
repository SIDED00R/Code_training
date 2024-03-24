import sys
input = sys.stdin.readline

def check(check_matrix, matrix, now, count):
    move = {"D" : [1, 0], "R" : [0, 1], "U" : [-1, 0], "L" : [0, -1]}
    now_i, now_j = now
    while check_matrix[now_i][now_j] == 0:
        di, dj = move[matrix[now_i][now_j]]
        check_matrix[now_i][now_j] = count
        now_i += + di
        now_j += dj
    if check_matrix[now_i][now_j] == count:
        return 1
    else:
        return 0

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(input().rstrip('\n'))
    matrix.append(line)

check_matrix = [[0 for _ in range(M)] for _ in range(N)]
count = 0
answer = 0

for i in range(N):
    for j in range(M):
        if not check_matrix[i][j]:
            count += 1
            answer += check(check_matrix, matrix, [i, j], count)
            
print(answer)
