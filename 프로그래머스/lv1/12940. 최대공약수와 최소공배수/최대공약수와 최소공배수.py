def gcd(n, m):
    while n != 0:
        n, m = m % n, n
    return m

def lcm(n, m):
    g = gcd(n, m)
    return n * m // g


def solution(n, m):
    n, m = min(n, m), max(n, m)
    g = gcd(n, m)
    l = lcm(n, m)
    return [g, l]