def count(x, y):
    answer = 0
    x, y = min(x, y), max(x, y)
    if x == 0:
        return 0
    if x % 2 == 0:
        n = x // 2
        answer += n * (2 * n + 1)
        answer += (y - x) // 2 * x
    else:
        n = x // 2
        answer += n * (2 * n + 1)
        answer += (y - x + 1) // 2 * x
    return answer

x1, y1, x2, y2 = map(int ,input().split())
print(count(x2, y2) - count(x1, y2) - count(x2, y1) + count(x1, y1))