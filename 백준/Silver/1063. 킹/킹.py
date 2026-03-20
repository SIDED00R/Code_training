k, r, n = input().split()
n = int(n)
move_dic = {"R":[1, 0], "L":[-1, 0], "B":[0, -1], "T":[0, 1], "RT":[1, 1], "LT":[-1, 1], "RB":[1, -1], "LB":[-1, -1]}
moves = []
for _ in range(n):
    moves.append(move_dic[input()])
dic = {chr(i + 65): i + 1 for i in range(8)}
r_dic = {i + 1: chr(i + 65) for i in range(8)}
k_now = [dic[k[0]], int(k[1])]
r_now = [dic[r[0]], int(r[1])]

matrix = [[0 for _ in range(9)] for _ in range(9)]
matrix[k_now[0]][k_now[1]] = "k"
matrix[r_now[0]][r_now[1]] = "r"

for move in moves:
    mx, my = move
    x, y = k_now
    nx = mx + x
    ny = my + y
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        if matrix[nx][ny] == 0:
            matrix[x][y] = 0
            matrix[nx][ny] = "k"
            k_now = [nx, ny]
        elif matrix[nx][ny] == "r":
            rx, ry = r_now
            nrx = rx + mx
            nry = ry + my
            if 1 <= nrx <= 8 and 1 <= nry <= 8:
                matrix[nrx][nry] = "r"
                matrix[rx][ry] = "k"
                matrix[x][y] = 0
                k_now = [nx, ny]
                r_now = [nrx, nry]

print(r_dic[k_now[0]] + str(k_now[1]))
print(r_dic[r_now[0]] + str(r_now[1]))
        
    