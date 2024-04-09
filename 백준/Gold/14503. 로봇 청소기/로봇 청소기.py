import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
count = 0

def move(room, i, j, d):
    global count
    if room[i][j] == 0:
        count += 1
        room[i][j] = 2
        
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    find = False
    for idx in range(4):
        next_i = i + di[idx]
        next_j = j + dj[idx]
        if 0 <= next_i < N and 0<= next_j < M and room[next_i][next_j] == 0:
            find = True
    if find:
        d = (d + 3) % 4
        if room[i + di[d]][j + dj[d]] == 0:
            move(room, i + di[d], j + dj[d], d)
        else:
            move(room, i, j, d)
    else:
        back = (d + 2) % 4
        if room[i + di[back]][j + dj[back]] != 1:
            move(room, i + di[back], j + dj[back], d)
    
N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = []
for _ in range(N):
    line = list(map(int, input().split()))
    room.append(line)
    
move(room, r, c, d)
print(count)