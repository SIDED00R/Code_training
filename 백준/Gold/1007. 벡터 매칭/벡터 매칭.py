from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())
    coordinate = []
    for _ in range(n):
        x, y = map(int, input().split())
        coordinate.append([x, y])
    answer = 1e20
    for now_case in combinations(range(n), n // 2):
        ans_x, ans_y = 0, 0
        for idx in range(n):
            nx, ny = coordinate[idx]
            if idx in now_case:
                ans_x += nx
                ans_y += ny
            else:
                ans_x -= nx
                ans_y -= ny
        answer = min(answer, (ans_x ** 2 + ans_y ** 2) ** 0.5)
    print(answer)