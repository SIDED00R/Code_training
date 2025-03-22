def time(t):
    dh = t[3] - t[0]
    dm = t[4] - t[1]
    ds = t[5] - t[2]
    if ds < 0:
        ds += 60
        dm -= 1
    if dm < 0:
        dm += 60
        dh -= 1
    return dh, dm, ds
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

a = time(a_list)
b = time(b_list)
c = time(c_list)
print(a[0], a[1], a[2])
print(b[0], b[1], b[2])
print(c[0], c[1], c[2])