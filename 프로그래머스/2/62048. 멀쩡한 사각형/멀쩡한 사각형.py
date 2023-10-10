import math

def gcd(m, n):
    while m != 0:
        m, n = n % m, m
    return n

def solution(w,h):
    
    if w == h:
        return w * h - w
    elif w == 1 or h == 1:
        return 0
    
    g = gcd(w, h)
    n, m = w // g, h // g

    K = m/n
    count = 0

    for i in range(n):
        count += math.ceil(K * (i + 1))- int(K * i)

    return w * h - count * g