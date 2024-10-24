def find(num):
    front = 0
    back = len(dots)
    while front <= back:
        mid = (front + back) // 2
        if dots[mid][0] < num:
            front = mid + 1
        else:
            back = mid - 1
    return front

n = int(input())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append([x, y])
q = int(input())
for _ in range(q):
    point = float(input())
    idx = find(point)
    if dots[idx][1] == dots[idx - 1][1]:
        print(0)
    elif dots[idx][1] > dots[idx - 1][1]:
        print(1)
    else:
        print(-1)