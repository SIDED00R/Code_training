import sys
from collections import deque
input = sys.stdin.readline

while True:
    try:
        L, A = map(int, input().split())
    except:
        break

    ants = []
    start_positions = []

    for _ in range(A):
        x_str, d = input().split()
        x = int(x_str)
        start_positions.append(x)

        if d == 'L':
            t = x
            side = 0   # left
        else:  # 'R'
            t = L - x
            side = 1   # right

        ants.append((t, side))

    start_positions.sort()
    labels = deque(start_positions)

    T = max(t for t, _ in ants)

    ants.sort(key=lambda x: x[0])

    idx = 0
    while idx < A and ants[idx][0] < T:
        _, side = ants[idx]
        if side == 0:
            labels.popleft()
        else:
            labels.pop()
        idx += 1

    last = []
    while idx < A and ants[idx][0] == T:
        _, side = ants[idx]
        if side == 0:
            last.append(labels.popleft())
        else:
            last.append(labels.pop())
        idx += 1

    last.sort()
    if len(last) == 1:
        print(f"The last ant will fall down in {T} seconds - started at {last[0]}.")
    else:
        print(f"The last ant will fall down in {T} seconds - started at {last[0]} and {last[1]}.")
