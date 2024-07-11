n, b, h, w = map(int, input().split())
find = False
for _ in range(h):
    p = int(input())
    line = list(map(int, input().split()))
    if n * p > b:
        continue
    for num in line:
        if num >= n:
            find = True
            b = n * p
            break
if find:
    print(str(b))
else:
    print("stay home")