import math

def triangle_area(x1, y1, x2, y2, x3, y3):
  area = 0.5 * abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
  return area

def get_line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom

    return (px, py)

def length(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

t = int(input())
for _ in range(t):
    bx, cx, cy, dx, dy = map(float, input().split())
    ax, ay, by = 0, 0, 0
    
    a_x, a_y = (bx + cx) / 2, (by + cy) / 2
    b_x, b_y = (cx + dx) / 2, (cy + dy) / 2
    c_x, c_y = (ax + dx) / 2, (ay + dy) / 2
    d_x, d_y = (ax + bx) / 2, (ay + by) / 2

    first = get_line_intersection(ax, ay, a_x, a_y, dx, dy, d_x, d_y)
    second = get_line_intersection(bx, by, b_x, b_y, ax, ay, a_x, a_y)
    third = get_line_intersection(cx, cy, c_x, c_y, bx, by, b_x, b_y)
    forth = get_line_intersection(dx, dy, d_x, d_y, cx, cy, c_x, c_y)

    answer_area = triangle_area(first[0], first[1], second[0], second[1], forth[0], forth[1]) + triangle_area(third[0], third[1], second[0], second[1], forth[0], forth[1])
    won = triangle_area(ax, ay, bx, by, second[0], second[1])
    zo = triangle_area(bx, by, cx, cy, third[0], third[1])
    su = triangle_area(cx, cy, dx, dy, forth[0], forth[1])
    suck = triangle_area(ax, ay, dx, dy, first[0], first[1])
    total_length = length(first[0], first[1], second[0], second[1]) + length(third[0], third[1], second[0], second[1]) + length(third[0], third[1], forth[0], forth[1]) + length(first[0], first[1], forth[0], forth[1])
    print(f"{won:.3f}", f"{zo:.3f}", f"{su:.3f}", f"{suck:.3f}", f"{answer_area:.3f}", math.ceil(total_length))
