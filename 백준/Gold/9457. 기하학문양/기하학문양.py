r = [1, 4]
rr = [1]

u = [1, 2]
for i in range(50000):
    before = r[-1]
    rr.append(rr[-1] + 2 * r[-2])
    r.append((before * 3 + rr[-1]) % 10007)
    u.append((u[-1] * 4 - u[-2]) % 10007)

t = int(input())
for _ in range(t):
    n = int(input())
    print(r[n - 1], n * (u[n] - 1) % 10007)