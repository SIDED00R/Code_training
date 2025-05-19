from fractions import Fraction

n, b = map(int, input().split())
total_x = 0
total_y = 0
for _ in range(n):
    x, y = map(int, input().split())
    total_x += x
    total_y += y

if total_x == 0:
    print("EZPZ")
else:
    top = total_y - n * b
    down = total_x
    print(Fraction(top, down))
    