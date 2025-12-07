from collections import defaultdict

def find(num):
    if parents[num] == num:
        return num
    else:
        return find(parents[num])

def union(a, b):
    a_p = find(a)
    b_p = find(b)
    if a_p != b_p:
        if a_p < b_p:
            parents[b_p] = a_p
        else:
            parents[a_p] = b_p
        return True
    else:
        return False

n = int(input())
x_cord = []
y_cord = []
z_cord = []
for idx in range(n):
    x, y, z = map(int, input().split())
    x_cord.append([x, idx])
    y_cord.append([y, idx])
    z_cord.append([z, idx])

x_cord = sorted(x_cord)
y_cord = sorted(y_cord)
z_cord = sorted(z_cord)

dic = defaultdict(list)
for idx in range(1, n):
    xb, xbi = x_cord[idx - 1]
    xn, xni = x_cord[idx]
    dic[abs(xb - xn)].append([xbi, xni])
    yb, ybi = y_cord[idx - 1]
    yn, yni = y_cord[idx]
    dic[abs(yb - yn)].append([ybi, yni])
    zb, zbi = z_cord[idx - 1]
    zn, zni = z_cord[idx]
    dic[abs(zb - zn)].append([zbi, zni])

parents = [i for i in range(n)]

answer = 0
for key in sorted(dic):
    for now_case in dic[key]:
        front, back = now_case
        if union(front, back):
            answer += key

print(answer)
    