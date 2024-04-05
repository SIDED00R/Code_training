import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def intersect(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    
    if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
        if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2):
            return 0
        if max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
            return 0
        return 1
    
    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        return 1
    return 0

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))

print(intersect(line1, line2))
