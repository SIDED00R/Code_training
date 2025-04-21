n, b = map(int, input().split())
max_b = 2 ** (b + 1) - 1
if n <= max_b:
    print("yes")
else:
    print('no')