x, y, d, t = map(int, input().split())
max_t = (x ** 2 + y ** 2) ** 0.5

able_time = max_t // d
answer = min(max_t, max_t - able_time * d + t * able_time, abs(max_t - d * (able_time + 1)) + t * (able_time + 1))
answer = min(answer, t * (max(able_time, 1) + 1))
print(answer)