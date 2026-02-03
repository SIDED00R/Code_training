n = int(input())
x = 0
y = 0
move = []
for _ in range(n):
    i, j = map(int, input().split())
    move.append([i, j])
    x += i
    y += j
print(x, y)
answer = 1e10
for idx in range(n):
    l = move[:idx] + move[idx + 1:]
    now_x, now_y = map(sum, zip(*l))
    length = round((now_x ** 2 + now_y ** 2) ** 0.5, 2)
    answer = min(length, answer)
print(f"{answer:.2f}")
    