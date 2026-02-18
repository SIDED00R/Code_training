n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    print(f"Scenario #{i + 1}:")
    total = sum([a, b, c])
    a, b = max(a, b, c), min(a, b, c)
    c = total - a - b
    if a ** 2 == b ** 2 + c ** 2:
        print("yes")
    else:
        print("no")
    print()