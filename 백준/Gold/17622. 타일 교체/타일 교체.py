import copy

def find_road(now_i, now_j, now_dir, m, n):
    move = {"D":[1, 0], "U":[-1, 0], "R":[0, 1], "L":[0, -1]}
    dic = {"D":["", "", "R", "L", "D", ""], "U":["R", "L", "", "", "U", ""], "L":["D", "", "U", "", "", "L"], "R":["", "D", "", "U", "", "R"]}
    count = 0
    while True:
        count += 1
        now_block = m[now_i][now_j]
        next_dir = dic[now_dir][now_block]
        if next_dir == "":
            return 1e9
        next_i = now_i + move[next_dir][0]
        next_j = now_j + move[next_dir][1]
        if next_i == n - 1 and next_j == n:
            return count
        elif 0 <= next_i < n and 0 <= next_j < n:
            now_i = next_i
            now_j = next_j
            now_dir = next_dir
        else:
            return 1e9


n, k = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)


answer = 1e9
if k == 0:
    answer = find_road(0, 0, "R", matrix, n)
else:
    for i in range(n):
        for j in range(n):
            for num in range(6):
                copy_matrix = copy.deepcopy(matrix)
                if matrix[i][j] != num:
                    copy_matrix[i][j] = num
                    now_count = find_road(0, 0, "R", copy_matrix, n)
                    answer = min(answer, now_count)

if answer == 1e9:
    print(-1)
else:
    print(answer)
