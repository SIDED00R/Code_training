def move(idx, tree):
    count = 0
    while idx != 1:
        if idx % 2 == 0:
            if count % 2 == 0:
                tree[idx // 2] = tree[idx] | tree[idx + 1]
            else:
                tree[idx // 2] = tree[idx] ^ tree[idx + 1]
        else:
            if count % 2 == 0:
                tree[idx // 2] = tree[idx] | tree[idx - 1]
            else:
                tree[idx // 2] = tree[idx] ^ tree[idx - 1]
        idx //= 2
        count += 1

n, m = map(int, input().split())
line = list(map(int, input().split()))
tree = [0] * (2 ** (n + 1))
for i in range(2 ** n):
    tree[2 ** n + i] = line[i]
for i in range(1, n + 1):
    for j in range(2 ** (n - i)):
        now = 2 ** (n - i) + j
        if i % 2 == 1:
            tree[now] = tree[now * 2] | tree[now * 2 + 1]
        else:
            tree[now] = tree[now * 2] ^ tree[now * 2 + 1]

for _ in range(m):
    p, b = map(int, input().split())
    now = 2 ** n + p - 1
    tree[now] = b
    move(now, tree)
    print(tree[1])