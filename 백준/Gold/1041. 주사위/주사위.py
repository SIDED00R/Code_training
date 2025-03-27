n = int(input())
a, b, c, d, e, f = list(map(int, input().split()))

if n == 1:
    print(sum([a, b, c, d, e, f]) - max(a, b, c, d, e, f))
    exit()

answer = 0

answer += min(a, b, c, d, e, f) * (4 * (n - 2) * (n - 1) + (n - 2) ** 2)
answer += min(a + b, a + d, a + c, a + e, f + e, f + d, f + b, f + c, b + d, d + e, e + c, c + b) * (4 * (n - 1) + 4 * (n - 2))
answer += min(a + b + d, a + d + e, a + e + c, a + c + b, f + b + d, f + d + e, f + e + c, f + c + b) * 4

print(answer)