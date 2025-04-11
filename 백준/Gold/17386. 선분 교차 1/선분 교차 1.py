import sys
input = sys.stdin.readline
from decimal import Decimal
from math import inf

epsilon = 1e-9

def line_from_points(p1, p2):
    if p2[0] - p1[0] != 0:
        m = Decimal(p2[1] - p1[1]) / Decimal(p2[0] - p1[0])
        b = p1[1] - m * p1[0]
        return m, b
    else:
        return inf, p1[0]

def intersection_point(m1, b1, m2, b2):
    if m1 == m2:
        return "parallel"
    if m1 == inf:
        x = b1
        y = m2 * x + b2
    elif m2 == inf:
        x = b2
        y = m1 * x + b1
    else:
        x = Decimal(b2 - b1) / Decimal(m1 - m2)
        y = m1 * x + b1
    return x, y

def is_point_on_segment(x, y, p1, p2):
    return min(p1[0], p2[0]) - epsilon <= x <= max(p1[0], p2[0]) + epsilon and min(p1[1], p2[1]) - epsilon <= y <= max(p1[1], p2[1]) + epsilon

def overlap(x0, x1, x2, x3):
    if x2 > x1 or x3 < x0:
        return 0
    else:
        return 1

dots = []
for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    dots.append([x1, y1])
    dots.append([x2, y2])
d0, d1, d2, d3 = dots
m1, b1 = line_from_points(d0, d1)
m2, b2 = line_from_points(d2, d3)

intersection = intersection_point(m1, b1, m2, b2)

if intersection == "parallel":
    if b1 == b2:
        if overlap(min(d0[0], d1[0]), max(d0[0], d1[0]), min(d2[0], d3[0]), max(d2[0], d3[0])):
            print(1)
        else:
            print(0)
    else:
        print(0)

else:
    x, y = intersection
    if is_point_on_segment(x, y, d0, d1) and is_point_on_segment(x, y, d2, d3):
        print(1)
    else:
        print(0)

