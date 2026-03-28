import sys
import math

input = sys.stdin.readline

n = int(input())
trees = []
total = 0

for _ in range(n):
    x, y, v = map(int, input().split())
    trees.append((x, y, v))
    total += v

PI = math.pi
EPS = 1e-15

critical = []
for i in range(n):
    x1, y1, _ = trees[i]
    for j in range(i + 1, n):
        x2, y2, _ = trees[j]
        dx = x2 - x1
        dy = y2 - y1

        ang = math.atan2(dy, dx) + PI / 2

        while ang < 0:
            ang += PI
        while ang >= PI:
            ang -= PI

        critical.append(ang)

critical.sort()

angles = []
for a in critical:
    if not angles or abs(angles[-1] - a) > EPS:
        angles.append(a)

answer = abs(total)


def check_angle(theta):
    global answer

    cx = math.cos(theta)
    cy = math.sin(theta)

    proj = []
    for x, y, v in trees:
        s = x * cx + y * cy
        proj.append((s, v))

    proj.sort()

    prefix = 0
    answer = min(answer, abs(total))
    for _, v in proj:
        prefix += v
        answer = min(answer, abs(total - 2 * prefix))


m = len(angles)

for i in range(m):
    a = angles[i]
    b = angles[i + 1] if i + 1 < m else angles[0] + PI
    mid = (a + b) / 2
    if mid >= PI:
        mid -= PI
    check_angle(mid)

print(answer)