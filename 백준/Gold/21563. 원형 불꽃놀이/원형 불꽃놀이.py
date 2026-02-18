def check(a, b, n):
    aw, ai = a
    bw, bi = b
    w_diff = bw - aw
    diff = min(bi - ai, n + ai - bi)
    if diff == 1:
        left = n - 3 - w_diff
        if left <= 0:
            return bw - n + 2
        else:
            return aw - 1 - left // 2
    else:
        left = n - 4 - w_diff
        if left <= 0:
            return bw - n + 2
        else:
            return aw - 2 - left // 2

n = int(input())
line = list(map(int, input().split()))
stack = sorted([line[i], i] for i in range(n))
answer = 1e10
for i in range(2):
    for idx in range(i + 1, 3):
        answer = min(answer, check(stack[i], stack[idx], n))

print(answer)