x, y, c = map(float, input().split())
front = 0
back = 1
for _ in range(100):
    mid = (front + back) / 2
    left = (c / (1 - mid)) ** 2 - (c / mid) ** 2 - x ** 2 + y ** 2
    if left < 0:
        front = mid
    else:
        back = mid
try:
    print(round((y ** 2 - (c / mid) ** 2) ** 0.5, 3))
except:
    print(0)