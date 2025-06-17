n, w, h = map(int, input().split())
for _ in range(n):
    num = int(input())
    if w ** 2 + h ** 2 >= num ** 2:
        print('DA')
    else:
        print("NE")