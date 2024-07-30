def input_data():
    global N, CMD, px, py, W, wall, Z, ZOMBI, D
    N = int(input().strip())
    CMD = input().strip()
    px, py = map(int, input().strip().split())
    W = int(input().strip())
    wall = [[0] * (N + 2) for _ in range(N + 2)]
    for _ in range(W):
        wx, wy = map(int, input().strip().split())
        wall[wx][wy] = 1
    Z = int(input().strip())
    ZOMBI = []
    for _ in range(Z):
        x, y, type_, dir_, speed = input().strip().split()
        ZOMBI.append({'x': int(x), 'y': int(y), 'type': int(type_), 'dir': dir_, 'speed': int(speed)})
    D = int(input().strip())


def move_player(dir):
    global px, py
    ndir = -1
    if dir == 'U':
        ndir = 0
    elif dir == 'R':
        ndir = 1
    elif dir == 'D':
        ndir = 2
    elif dir == 'L':
        ndir = 3
    elif dir == 'S':
        return

    nx = px + dir_x[ndir]
    ny = py + dir_y[ndir]
    if 1 <= nx <= N and 1 <= ny <= N and wall[nx][ny] == 0:
        px = nx
        py = ny


def cnt_wall(x, y, p):
    cnt = 0
    nx = x
    ny = y
    while True:
        if not (1 <= nx + dir_x[p] <= N) or not (1 <= ny + dir_y[p] <= N):
            break
        if wall[nx + dir_x[p]][ny + dir_y[p]] == 1:
            cnt += 1
        nx += dir_x[p]
        ny += dir_y[p]
    return cnt


def move_zombies():
    global zpos, ZOMBI
    zpos = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(Z):
        type_ = ZOMBI[i]['type']
        dir_ = ZOMBI[i]['dir']
        ndir = -1
        speed = ZOMBI[i]['speed']

        if dir_ == 'U':
            ndir = 0
        elif dir_ == 'R':
            ndir = 1
        elif dir_ == 'D':
            ndir = 2
        elif dir_ == 'L':
            ndir = 3

        if type_ == 0:
            nx = ZOMBI[i]['x']
            ny = ZOMBI[i]['y']
            for s in range(1, speed + 1):
                if not (1 <= nx + dir_x[ndir] <= N) or not (1 <= ny + dir_y[ndir] <= N):
                    ndir = dir_op[ndir]
                    break
                if wall[nx + dir_x[ndir]][ny + dir_y[ndir]] == 1:
                    ndir = dir_op[ndir]
                    break
                nx += dir_x[ndir]
                ny += dir_y[ndir]

            if ndir == 0:
                dir_ = 'U'
            elif ndir == 1:
                dir_ = 'R'
            elif ndir == 2:
                dir_ = 'D'
            elif ndir == 3:
                dir_ = 'L'

            ZOMBI[i] = {'x': nx, 'y': ny, 'type': type_, 'dir': dir_, 'speed': speed}
            zpos[nx][ny] = 1

        elif type_ == 1:
            nx = ZOMBI[i]['x']
            ny = ZOMBI[i]['y']
            for h in range(1, speed + 1):
                if not (1 <= nx + dir_x[ndir] <= N) or not (1 <= ny + dir_y[ndir] <= N):
                    break
                if wall[nx + dir_x[ndir]][ny + dir_y[ndir]] == 1:
                    wall[nx + dir_x[ndir]][ny + dir_y[ndir]] = 0
                    break
                nx += dir_x[ndir]
                ny += dir_y[ndir]

            max_cnt = -1
            opt_dir = -1
            for p in range(4):
                res = cnt_wall(nx, ny, p)
                if res > max_cnt:
                    max_cnt = res
                    opt_dir = p

            nopt_dir = '-1'
            if opt_dir == 0:
                nopt_dir = 'U'
            elif opt_dir == 1:
                nopt_dir = 'R'
            elif opt_dir == 2:
                nopt_dir = 'D'
            elif opt_dir == 3:
                nopt_dir = 'L'

            ZOMBI[i] = {'x': nx, 'y': ny, 'type': type_, 'dir': nopt_dir, 'speed': speed}
            zpos[nx][ny] = 1


def simulation():
    global dead_day
    for day in range(1, D + 1):
        if day - 1 >= len(CMD):
            break
        move_player(CMD[day - 1])
        move_zombies()
        if zpos[px][py] == 1:
            dead_day = day
            return False
    return True


dir_x = [-1, 0, 1, 0]
dir_y = [0, 1, 0, -1]
dir_op = [2, 3, 0, 1]

input_data()
if not simulation():
    print(dead_day)
    print("DEAD...")
else:
    print("ALIVE!")