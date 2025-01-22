import sys

input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

count = 0
for num in line:
    if num % 2 != 0:
        count += 1

if count == 0 and len(line) == 1:
    print(0)
    exit()
if count == 2 and line[0] * line[-1] % 2 != 0:
    print(0)
else:
    print(1)
