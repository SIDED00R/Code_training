r, c, k = map(int, input().split())
if k == 1:
    print(1)
elif r % 2 == 0 or c % 2 == 0:
    print(1)
else:
    print(0)