import sys
input = sys.stdin.readline

n, m = map(int, input().split())
line = list(map(int, input().split()))

stack = []
for idx in range(n):
    stack.append([line[idx], idx + 1])

stack.sort(reverse = True)
success = True

for i in range(min(3, n - 1)):
    if stack[i][0] > stack[i + 1][0] + m:
        success = False
        break

if success:
    print('YES')
    for i in range(n):
        if i == 2 or i == 3:
            continue
        print(f'{stack[i][1]} ')
    for i in range(2, min(n, 4)):
        print(f'{stack[i][1]} ')
else:
    print('NO')