def f(l):
    return l[0] * 6 + l[1] * 3 + l[2] * 2 + l[3] + l[4] * 2
v = list(map(int, input().split()))
h = list(map(int, input().split()))
print(f(v), f(h))
