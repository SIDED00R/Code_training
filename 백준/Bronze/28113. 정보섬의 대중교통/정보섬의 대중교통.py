n, a, b = map(int, input().split())
if b > a:
    print("Bus")
elif b == a:
    print("Anything")
else:
    print("Subway")