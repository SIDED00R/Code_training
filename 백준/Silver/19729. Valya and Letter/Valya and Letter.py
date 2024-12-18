def find(n, h):
    count = 0
    while h < n:
        count += 1
        h *= 2
    return count

n, m, h, w = map(int, input().split())
n, m = min(m, n), max(m, n)
h, w = min(h, w), max(h, w)

answer1 = 0
if h < n:
    answer1 += find(n, h)
if w < m:
    answer1 += find(m, w)

answer2 = 0
if h < m:
    answer2 += find(m, h)
if w < n:
    answer2 += find(n, w)
print(min(answer1, answer2))