a, b = map(int, input().split())
c = int(input())
total = a + b
if a + b >= c * 2:
    print(a + b - 2 * c)
else:
    print(a + b)