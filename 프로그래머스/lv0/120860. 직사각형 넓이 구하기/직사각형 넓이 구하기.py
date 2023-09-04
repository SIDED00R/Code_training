def solution(dots):
    point = dots[0]
    for dot in dots[1:]:
        if dot[0] == point[0]:
            vertical = abs(dot[1] - point[1])
        elif dot[1] == point[1]:
            horizon = abs(dot[0] - point[0])
    return vertical * horizon