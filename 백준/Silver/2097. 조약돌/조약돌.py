n = int(input())
if n <= 2:
    print(4)
    exit()
side = int(n ** 0.5)
small = side ** 2
left = n - small
if left == 0:
    print(4 * side - 4)
elif left > side:
    print(4 * side)
else:
    print(4 * side - 2)
