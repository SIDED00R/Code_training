n = int(input())
coordinate = []
x_c = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append([x, y])
    x_c.append(x)
coordinate.sort()
x_c = sorted(x_c)

answer = 1e20
if n == 2:
    print(4)
    exit()
for i in range(len(x_c)):
    for j in range(i + 1, len(x_c)):
        x_low = x_c[i] - 1
        x_high = x_c[j] + 1
        y_stack = []
        for x, y in coordinate:
            if x_low < x < x_high:
                y_stack.append(y)
        if len(y_stack) < n // 2:
            continue
        y_stack = sorted(y_stack)
        for idx in range(len(y_stack) - n // 2 + 1):
            y_low = y_stack[idx] - 1
            y_high = y_stack[idx + n // 2 - 1] + 1
            answer = min(answer, (x_high - x_low) * (y_high - y_low))
print(answer)