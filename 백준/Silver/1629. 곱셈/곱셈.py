import sys
input = sys.stdin.readline

A, B, C = map(int, input().rstrip('\n').split())

def devide(a, b, c):
    if b == 1:
        return a % c
    half = devide(a, b // 2, c)
    if b % 2:
        return half ** 2 * a % c
    else:
        return half ** 2 % c
        
print(devide(A, B, C))