import sys
from bisect import bisect_left

input = sys.stdin.readline

A, B = map(int, input().split())
T = A - B + 1

N = int(input())
L = [0]*(N+1)
R = [0]*(N+1)

best_val = 10**30
best_x = -1
best_y = -1

rights = []

for i in range(1, N+1):
    li, ri = map(int, input().split())
    L[i] = li
    R[i] = ri
    rights.append((ri, i))

if T <= 0:
    print(-1, -1)
    sys.exit()

for i in range(1, N+1):
    li = L[i]
    if li >= T and li < best_val:
        best_val = li
        best_x, best_y = i, -1

for i in range(1, N+1):
    ri = R[i]
    if ri >= T and ri < best_val:
        best_val = ri
        best_x, best_y = -1, i

rights.sort()
r_vals = [rv for rv, _ in rights]   # bisect용

for i in range(1, N+1):
    need = T - L[i]
    if need <= 0:
        continue

    pos = bisect_left(r_vals, need)
    if pos >= N:
        continue

    rv, j = rights[pos]
    if j != i:
        val = L[i] + rv
        if val < best_val:
            best_val = val
            best_x, best_y = i, j
    else:
        pos2 = pos + 1
        if pos2 < N:
            rv2, j2 = rights[pos2]
            val = L[i] + rv2
            if val < best_val:
                best_val = val
                best_x, best_y = i, j2

if best_val == 10**30:
    print("No")
else:
    print(best_x, best_y)
