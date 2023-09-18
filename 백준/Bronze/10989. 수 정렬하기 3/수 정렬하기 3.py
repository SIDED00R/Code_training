import sys

n = int(sys.stdin.readline())

stack = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    stack[num] += 1

for i in range(10001):
    if stack[i] != 0:
        for _ in range(stack[i]):
            print(i)
