def length(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2

def check(stack):
    xs, ys = zip(*stack)
    x, y = stack[0]
    mid_x = sum(xs) / 4
    mid_y = sum(ys) / 4
    find = False
    our = []
    other = []
    for idx in range(1, 4):
        nx, ny = stack[idx]
        if (nx + x) / 2 == mid_x and (ny + y) / 2 == mid_y:
            find = True
            our.append([nx, ny])
        else:
            other.append([nx, ny])

    if not find:
        return False
    if length(stack[0], other[0]) == length(stack[0], other[1]) and length(stack[0], our[0]) == length(other[0], other[1]):
        return True
    else:
        return False
    
t = int(input())
for _ in range(t):
    stack = []
    for _ in range(4):
        x, y = map(int, input().split())
        stack.append([x, y])
    if check(stack):
        print(1)
    else:
        print(0)