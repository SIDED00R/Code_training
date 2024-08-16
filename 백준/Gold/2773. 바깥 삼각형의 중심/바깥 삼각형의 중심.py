def add_points(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

def cross_product(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def ort(p1, p2, p3):
    d = (p1[0] + p2[1] - p1[1], p1[1] + p1[0] - p2[0])
    e = (p1[0] + p1[1] - p2[1], p1[1] + p2[0] - p1[0])
    if ccw(p1, p2, p3) * ccw(p1, p2, d) < 0:
        return d
    else:
        return e

def cr(p1, p2, p3, p4):
    ab = (p2[0] - p1[0], p2[1] - p1[1])
    cd = (p4[0] - p3[0], p4[1] - p3[1])
    t = (cross_product(p3, cd) - cross_product(p1, cd)) / cross_product(ab, cd)
    x = p1[0] + ab[0] * t
    y = p1[1] + ab[1] * t
    return (x, y)

def test():
    ax, ay = map(float, input().split())
    bx, by = map(float, input().split())
    cx, cy = map(float, input().split())
    
    a = (ax, ay)
    b = (bx, by)
    c = (cx, cy)

    d = ort(a, b, c)
    g = ort(a, c, b)
    e = ort(b, a, c)
    j = ort(b, c, a)
    
    o = cr(add_points(d, g), a, add_points(e, j), b)
    print(f"{o[0]:.4f} {o[1]:.4f}")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        test()