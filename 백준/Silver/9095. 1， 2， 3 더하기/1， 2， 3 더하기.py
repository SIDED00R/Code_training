import sys
input = sys.stdin.readline

def find(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return find(n - 2) + find(n - 1) + find(n - 3)

N = int(input())

for _ in range(N):
    num = int(input())
    print(find(num))
    