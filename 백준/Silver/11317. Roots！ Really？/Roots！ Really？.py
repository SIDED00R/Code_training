
n = int(input())
for _ in range(n):
    a, b, c, s, t = map(int, input().split())
    check = b ** 2 - 4 * a * c
    if check >= 0:
        first = (-b + check ** 0.5) / (2 * a)
        second = (-b - check ** 0.5) / (2 * a)
        if s <= first <= t or s <= second <= t:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
