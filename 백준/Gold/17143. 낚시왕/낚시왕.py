from collections import defaultdict
import sys
input = sys.stdin.readline

def move(r, c, s, d, R, C):
    if d == 1 or d == 2:
        if R > 1:
            s %= (R - 1) * 2
        else:
            s = 0
        nr = r + (-s if d == 1 else s)
        nd = d
        while nr < 1 or nr > R:
            if nr < 1:
                nr = 2 - nr
                nd = 2
            elif nr > R:
                nr = 2 * R - nr
                nd = 1
        return nr, c, nd
    else:
        if C > 1:
            s %= (C - 1) * 2
        else:
            s = 0
        nc = c + (s if d == 3 else -s)
        nd = d
        while nc < 1 or nc > C:
            if nc < 1:
                nc = 2 - nc
                nd = 3 
            elif nc > C:
                nc = 2 * C - nc
                nd = 4
        return r, nc, nd

R, C, M = map(int, input().split())

sharks = dict()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r, c)] = [s, d, z]

answer = 0
for fisher_col in range(1, C + 1):
    catch_pos = None
    catch_row = 10**9
    for (r, c) in sharks.keys():
        if c == fisher_col and r < catch_row:
            catch_row = r
            catch_pos = (r, c)
    if catch_pos is not None:
        answer += sharks[catch_pos][2]  # z
        del sharks[catch_pos]

    new_sharks = dict()
    for (r, c), (s, d, z) in sharks.items():
        nr, nc, nd = move(r, c, s, d, R, C)
        if (nr, nc) in new_sharks:
            if z > new_sharks[(nr, nc)][2]:
                new_sharks[(nr, nc)] = [s, nd, z]
        else:
            new_sharks[(nr, nc)] = [s, nd, z]
    sharks = new_sharks

print(answer)
