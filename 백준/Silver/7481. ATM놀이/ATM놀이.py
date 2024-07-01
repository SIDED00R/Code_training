n = int(input())

for _ in range(n):
    a, b, s = map(int, input().split())
    if a > b:
        change = True
    else:
        change = False
    a, b = min(a, b), max(a, b)
    q = s // b
    find = False
    for i in range(a):
        left = s - q * b
        if left % a == 0:
            find = True
            answer = [left // a, q]
            break
        q -= 1
        if q < 0:
            break
    if find:
        if change:
            print(answer[1], answer[0])
        else:
            print(answer[0], answer[1])
    else:
        print("Impossible")