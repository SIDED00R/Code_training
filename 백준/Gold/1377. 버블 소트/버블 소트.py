import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append((int(input()), i))

arr = sorted(arr)

ans = 0
for i in range(N):
    ans = max(ans, arr[i][1]-i)

print(ans+1)