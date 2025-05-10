a, b = map(int, input().split('/'))

while a != 1 or b != 1:
    if a > b:
        print("R", end = "")
        a, b = b, (a - b)
    else:
        print("L", end = "")
        a, b = (b - a), a