n, k = map(int, input().split())
stack = [0 for _ in range(n * 2 + 1)]
for idx in range(1, 2 * n + 1):
    if stack[idx] == 0:
        stack[idx] = stack[idx - 1] + 1
        next_idx = idx * 2
        while next_idx < 2 * n + 1:
            stack[next_idx] = stack[idx - 1] + 1
            next_idx *= 2

for idx in range(n, 2 * n + 1):
    if stack[idx] <= k:
        print(idx - n)
        break