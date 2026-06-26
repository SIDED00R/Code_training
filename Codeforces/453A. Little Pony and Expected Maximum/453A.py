def calc(m, n):
    s = 0.0
    j = 1
    while j < m:
        term = ((m - j) / m) ** n
        if term < 0.000001:
            break
        s += term
        j += 1
    return m - s

m, n = map(int, input().split())
print(calc(m, n))