t = int(input())
for i in range(t):
    line = list(map(int, input().split()))
    line = sorted(line)
    if line[2] >= line[1] + line[0]:
        print(f"Case #{i + 1}: invalid!")
        continue
    test = set(line)
    if len(test) == 3:
        print(f"Case #{i + 1}: scalene")
    elif len(test) == 2:
        print(f"Case #{i + 1}: isosceles")
    elif len(test) == 1:
        print(f"Case #{i + 1}: equilateral")
        