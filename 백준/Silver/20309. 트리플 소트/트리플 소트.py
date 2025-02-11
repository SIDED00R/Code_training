import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

answer = True
for idx in range(n):
    if (idx % 2 == 0 and line[idx] % 2 == 1) or (idx % 2 == 1 and line[idx] % 2 == 0):
        continue
    else:
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")
