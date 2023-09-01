def tangent(dot1, dot2):
    x = dot1[0] - dot2[0]
    y = dot1[1] - dot2[1]
    return y/x

def solution(dots):
    if tangent(dots[0],dots[1]) == tangent(dots[2],dots[3]) or tangent(dots[0],dots[2]) == tangent(dots[1],dots[3]) or tangent(dots[0],dots[3]) == tangent(dots[2],dots[1]):
        return 1
    return 0