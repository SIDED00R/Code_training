import math

time = int(input())
a = time // 300
time %= 300
b = time // 60
time %= 60
if time % 10 != 0:
    print(-1)
    exit()
else:
    print(a, b, time // 10)