n = int(input())

base = (n - 3) // 3

left = n - 3 * base

while left >= 6:
    base += 1
    left -= 3

if left == 3:
    print(base, base + 1, base + 2)
elif left == 4:
    print(base, base + 1, base + 3)
else:
    print(base, base + 2, base + 3)
