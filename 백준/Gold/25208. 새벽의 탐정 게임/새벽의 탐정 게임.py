import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

si = sj = ei = ej = -1
for i in range(n):
    for j in range(m):
        if board[i][j] == 'D':
            si, sj = i, j
            board[i][j] = '.'
        elif board[i][j] == 'R':
            ei, ej = i, j
            board[i][j] = '.'

# 상태: (bottom, down, right, up, left, top)
init = (0, 1, 2, 3, 4, 5)

# 우, 좌, 하, 상 이동 시 면 재배치
next_node = [
    [2, 1, 5, 3, 0, 4],  # right
    [4, 1, 0, 3, 5, 2],  # left
    [1, 5, 2, 0, 4, 3],  # down
    [3, 0, 2, 5, 4, 1],  # up
]

def roll(state, d):
    mp = next_node[d]
    return (
        state[mp[0]],
        state[mp[1]],
        state[mp[2]],
        state[mp[3]],
        state[mp[4]],
        state[mp[5]],
    )

# 주사위의 가능한 24개 방향 상태를 전부 생성
state_id = {init: 0}
states = [init]
trans = []

q = deque([init])
while q:
    cur = q.popleft()
    cur_id = state_id[cur]
    if len(trans) <= cur_id:
        trans.append([0] * 4)

    for d in range(4):
        nxt = roll(cur, d)
        if nxt not in state_id:
            state_id[nxt] = len(states)
            states.append(nxt)
            q.append(nxt)
        trans[cur_id][d] = state_id[nxt]

# 실제로 24개인지 확인 가능
# print(len(states))  # 24

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

visited = [[[-1] * len(states) for _ in range(m)] for _ in range(n)]
start_sid = 0
visited[si][sj][start_sid] = 0

q = deque([(si, sj, start_sid)])

while q:
    i, j, sid = q.popleft()
    dist = visited[i][j][sid]

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if not (0 <= ni < n and 0 <= nj < m):
            continue
        if board[ni][nj] == '#':
            continue

        nsid = trans[sid][d]

        # 도착 칸이면 바닥 면이 0인지 확인
        if ni == ei and nj == ej:
            if states[nsid][0] == 0:
                print(dist + 1)
                sys.exit(0)
            continue

        if visited[ni][nj][nsid] == -1:
            visited[ni][nj][nsid] = dist + 1
            q.append((ni, nj, nsid))

print(-1)