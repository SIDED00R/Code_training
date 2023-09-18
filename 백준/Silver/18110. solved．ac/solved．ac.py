import sys

def newround(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(sys.stdin.readline())

if n:
    notnormal = newround(n * 0.15)

    arr = [int(sys.stdin.readline()) for _ in range(n)]
    arr.sort()

    print(newround(sum(arr[notnormal:n - notnormal])/(n - notnormal * 2)))
else:
    print(0)