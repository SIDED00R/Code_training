import sys
input = sys.stdin.readline

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

count = int(input())
for _ in range(count):
    find = False
    N, M, x, y = map(int, input().rstrip('\n').split())
    lcm = N * M // gcd(N, M)
    for i in range(1, M + 1):
        if (y - x + i * N) % M == 0:
            print(lcm - N * i + x)
            find = True
            break
    if not find:
        print(-1)