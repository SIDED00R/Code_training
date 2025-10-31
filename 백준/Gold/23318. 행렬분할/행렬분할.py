import sys
from itertools import combinations

def build_psum(mat):
    n, m = len(mat), len(mat[0])
    ps = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        row = mat[i-1]
        for j in range(1, m+1):
            ps[i][j] = row[j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]
    return ps

def rect_sum(ps, r1, c1, r2, c2):
    return ps[r2][c2] - ps[r1-1][c2] - ps[r2][c1-1] + ps[r1-1][c1-1]

def feasible(ps, n, m, a, b, T):
    from itertools import combinations
    for rows in combinations(range(1, n), a):
        rcuts = [0] + list(rows) + [n]
        vcuts = 0
        strip_sums = [0] * (a + 1)
        c = 1
        ok = True
        while c <= m:
            overflow = False
            col_adds = []
            for k in range(a + 1):
                r1 = rcuts[k] + 1
                r2 = rcuts[k+1]
                col_add = ps[r2][c] - ps[r1-1][c] - ps[r2][c-1] + ps[r1-1][c-1]
                col_adds.append(col_add)
                if col_add > T:
                    ok = False
                    overflow = True
                    break
            if not ok:
                break

            for k in range(a + 1):
                if strip_sums[k] + col_adds[k] > T:
                    overflow = True
                    break

            if overflow:
                vcuts += 1
                if vcuts > b:
                    ok = False
                    break
                strip_sums = [0] * (a + 1)
            else:
                for k in range(a + 1):
                    strip_sums[k] += col_adds[k]
                c += 1

        if ok:
            return True
    return False


def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a, b = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    ps = build_psum(mat)
    lo = max(max(row) for row in mat)      
    hi = ps[n][m]                   
    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(ps, n, m, a, b, mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)

solve()
